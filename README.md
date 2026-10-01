# EduGenie – Google Gemini Powered Learning Assistant

A self-contained FastAPI learning assistant demo.

Features:
- Topic-based learning
- Beginner / Intermediate / Advanced levels
- Explanations
- Notes
- Quiz generation
- 7-day study plan
- Runs without an API key

## Windows
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000
