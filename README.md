# Black Metal Radio

A web application that randomly selects black metal bands from a curated list and plays their music through YouTube integration.

## Features

- Random black metal band selection from a curated list
- YouTube video integration for each band
- Clean, minimalist dark interface

## Tech Stack

- Python 3.9
- Flask 2.0.1
- Google Cloud Run
- YouTube Data API v3
- Gunicorn

## Prerequisites

- Python 3.9 or higher
- Google Cloud Platform account
- YouTube Data API key

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/blackmetalradio.git
cd blackmetalradio
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```
YOUTUBE_API_KEY=your_youtube_api_key
```

5. Run the application locally:
```bash
python app.py
```

The application will be available at `http://localhost:8080`

## Acknowledgments

- The black metal community
- YouTube Data API
- Google Cloud Platform 
