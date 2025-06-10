# Black Metal Radio

A web application that randomly selects black metal bands and plays their music through YouTube integration. Built with Flask and deployed on Google Cloud Run.

## Features

- Random black metal band selection from a curated list
- YouTube video integration for each band
- Clean, minimalist dark interface
- Serverless deployment on Google Cloud Run

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

## Deployment

1. Build and push the container:
```bash
gcloud builds submit --tag gcr.io/metalradio/blackmetalradio
```

2. Deploy to Cloud Run:
```bash
gcloud run deploy blackmetalradio \
  --image gcr.io/metalradio/blackmetalradio \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## Project Structure

```
blackmetalradio/
├── app.py              # Main application file
├── bands.csv           # List of black metal bands
├── Dockerfile          # Container configuration
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   └── index.html     # Main page template
└── README.md          # This file
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The black metal community
- YouTube Data API
- Google Cloud Platform 