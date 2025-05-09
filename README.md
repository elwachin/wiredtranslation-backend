# LanguageWire Translation API

Backend service for the LanguageWire Full Stack ML Engineer Challenge providing translation services:

- Translation of "Hello. How are you?" into 5 supported languages
- Translation of any text into Jeringoza

## 🚀 Setup & Installation

### Prerequisites
- Python 3.9+

### Installation
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ��‍♂️ Running the API
```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at http://localhost:8000

## 📝 API Documentation

### 1. Standard Translation Endpoint

**Endpoint:** POST /translate

**Supported languages:** spanish, german, french, italian, danish

**Example Request:**
```bash
curl -X POST http://localhost:8000/translate \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello. How are you?", "language": "french"}'
```

**Example Response:**
```json
{
  "translated": "Bonjour. Comment ça va?"
}
```

### 2. Jeringoza Translation Endpoint

**Endpoint:** POST /jeringoza

**Example Request:**
```bash
curl -X POST http://localhost:8000/jeringoza \
     -H "Content-Type: application/json" \
     -d '{"text": "hello"}'
```

**Example Response:**
```json
{
  "translated": "hepelopo"
}
```