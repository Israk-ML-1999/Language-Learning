# Language Learning System

An AI-powered language learning system with pronunciation assessment and custom phrase management.

## Features

- **Pronunciation Recording & Assessment**
  - AI-based pronunciation scoring
  - Visual feedback for pronunciation errors
  - Speech recognition integration

- **Custom Phrase Management**
  - User-created phrase cards
  - AI-powered phrase suggestions
  - Categorization system

- **AI Integration**
  - OpenAI API integration
  - Smart content recommendations
  - Automated feedback generation

## Technical Stack

- FastAPI
- OpenAI API
- SQLite Database
- Python 3.8+
- Speech Recognition

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file with your configuration:
   ```
   OPENAI_API_KEY=your-openai-api-key
   SECRET_KEY=your-secret-key
   ```

6. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

## API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
app/
├── api/
│   └── routes/
│       ├── phrases.py
│       └── pronunciation.py
├── core/
│   └── config.py
├── models/
│   ├── phrases.py
│   └── pronunciation.py
├── services/
│   ├── ai_service.py
│   └── pronunciation_service.py
└── main.py
```

## License

MIT License
