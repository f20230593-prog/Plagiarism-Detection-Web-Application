import os
import random
import requests
import pdfplumber
from docx import Document
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.staticfiles import StaticFiles

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_random_phrases(text, num_phrases=5, phrase_len=7):
    words = text.split()
    phrases = []
    for _ in range(num_phrases):
        idx = random.randint(0, len(words) - phrase_len)
        phrase = " ".join(words[idx:idx+phrase_len])
        phrases.append(phrase)
    return phrases

def search_serpapi(query):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 5
    }
    r = requests.get(url, params=params)
    data = r.json()
    return [res['link'] for res in data.get("organic_results", []) if 'link' in res]

def clean_html_content(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
            tag.decompose()
        return soup.get_text(separator=' ', strip=True)
    except Exception:
        return ""

def get_similarity(text1, text2):
    vect = TfidfVectorizer().fit_transform([text1, text2])
    return cosine_similarity(vect[0:1], vect[1:2])[0][0] * 100

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename.lower()
    if not (filename.endswith(".docx") or filename.endswith(".pdf")):
        return JSONResponse({"error": "Only .docx and .pdf files are supported"}, status_code=400)

    file_bytes = await file.read()
    with open("temp_upload", "wb") as f:
        f.write(file_bytes)

    if filename.endswith(".docx"):
        content = extract_text_from_docx("temp_upload")
    else:
        content = extract_text_from_pdf("temp_upload")

    phrases = extract_random_phrases(content)
    results = []

    for phrase in phrases:
        urls = search_serpapi(phrase)
        for url in urls:
            web_text = clean_html_content(url)
            sim = get_similarity(content, web_text)
            if sim > 10:
                results.append({
                    "phrase": phrase,
                    "url": url,
                    "similarity": round(sim, 2)
                })

    avg_similarity = round(sum([r["similarity"] for r in results]) / len(results), 2) if results else 0.0
    os.remove("temp_upload")
    return {"average_similarity": avg_similarity, "matches": results}