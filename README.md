# 📄 Plagiarism Detection Web Application

## 📝 Summary

The idea for this project originates from a common problem faced in academia, research, and content creation — **plagiarism**.  
Students, writers, researchers, and organizations often struggle to ensure originality in their work. While plagiarism checkers exist, many are expensive, closed-source, or lack flexibility for integration into custom workflows.

Our **Plagiarism Detection Web Application** solves this problem by offering a **free, accessible, and developer-friendly platform** for detecting plagiarism in multiple file formats (TXT, DOCX, PDF).  
It analyzes text using **AI-powered similarity algorithms** (TF-IDF + cosine similarity), highlights matching portions, and calculates a plagiarism score.  

The system allows:
- **Users** to upload or paste content and instantly check for plagiarism.
- **Custom corpus checking** — compare against local documents.
- **Optional web scraping** to detect matches from online sources.
- **PDF/DOCX parsing** for easy academic use.

---

## 📸 Features

- 📂 **Multi-format support**: `.txt`, `.docx`, `.pdf`  
- 🖍 **Highlighting plagiarized text** in results  
- 📊 **Similarity percentage** calculation  
- 🌍 **Optional online source checking** using BeautifulSoup4 + Requests  
- 📑 **Downloadable plagiarism report**  
- 🖥 **Responsive HTML UI** (Jinja2 templates)  
- ⚡ **Fast API responses** with [FastAPI](https://fastapi.tiangolo.com/) backend  
- 🛡 **Input sanitization** and file type restrictions  

---

## 🏆 Achievements

- Designed as a **lightweight, open-source alternative** to commercial plagiarism checkers.  
- **Fast processing** even for large documents thanks to efficient TF-IDF vectorization.  
- Supports **integration with other platforms** via REST API.

---

## 🛠 Tech Stack

**Frontend:**  
- HTML5, CSS3, JavaScript  
- Jinja2 templates (dynamic HTML rendering)

**Backend:**  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [Uvicorn](https://www.uvicorn.org/)  
- [scikit-learn](https://scikit-learn.org/) (TF-IDF, cosine similarity)

**Parsing & Processing:**  
- [`python-docx`](https://python-docx.readthedocs.io/) for DOCX files  
- [`pdfplumber`](https://github.com/jsvine/pdfplumber) for PDFs  
- [`beautifulsoup4`](https://www.crummy.com/software/BeautifulSoup/) + [`requests`](https://pypi.org/project/requests/) for optional web scraping  

**Config & Environment:**  
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) for environment variables  

---

## 🚀 Getting Started

### 📦 Clone the Repository

git clone https://github.com/f20230593-prog/Plagiarism-Detection-Web-Application
cd Plagiarism-Detection-Web-Application



Setup Python Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install Dependencies
pip install -r requirements.txt

 Run the Application
 uvicorn main:app --reload
http://127.0.0.1:8000

API Endpoints
POST /upload
Upload a file or raw text for plagiarism checking.

Request (multipart/form-data):

file: <uploaded_file>  # TXT, DOCX, or PDF
or

arduino

text: "Your text here..."
Response (JSON):

json

{
  "similarity_score": 78.3,
  "plagiarized_sections": [
    {"text": "sample matched phrase", "source": "source_url_or_id"}
  ]
}
📊 AI Output Fields
Similarity Score → Percentage match with existing sources

Matched Phrases → Highlighted portions of copied text

Sources → URLs or document IDs from which the text matches

📁 Project Structure
bash

Plagiarism-Detection-Web-Application/
│
├── main.py                # FastAPI app entry point
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── requirements.txt       # Dependencies
└── README.md              # Documentation
🧪 Sample JSON Response
json

{
  "similarity_score": 65.0,
  "plagiarized_sections": [
    {
      "text": "This is an exact copied section",
      "source": "https://example.com/source1"
    },
    {
      "text": "Another matched part",
      "source": "local_database_document_42"
    }
  ]
}
✨ Contributors
👨‍💻 Suyash Mangla – Backend, NLP, API Development
🎨 Kaggle – Frontend, UI/UX

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

