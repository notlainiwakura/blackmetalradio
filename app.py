from flask import Flask, render_template, jsonify
import random
import csv
import os
import logging
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
load_dotenv()

def get_random_band():
    try:
        logger.info("Attempting to read bands.csv")
        with open('bands.csv', 'r', encoding='utf-8') as file:
            # Read the first line and split by comma
            bands = file.readline().strip().split(',')
            # Filter out any empty strings
            bands = [band.strip() for band in bands if band.strip()]
            logger.info(f"Successfully read {len(bands)} bands from file")
            return random.choice(bands)
    except Exception as e:
        logger.error(f"Error reading bands.csv: {e}")
        return "Error loading band"

def search_youtube(query):
    try:
        api_key = os.getenv('YOUTUBE_API_KEY')
        if not api_key:
            logger.warning("YOUTUBE_API_KEY not set")
            return None
            
        logger.info(f"Searching YouTube for: {query}")
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        request = youtube.search().list(
            part='snippet',
            q=query + ' black metal',
            type='video',
            maxResults=1
        )
        response = request.execute()
        
        if response['items']:
            video_id = response['items'][0]['id']['videoId']
            logger.info(f"Found video ID: {video_id}")
            return f'https://www.youtube.com/watch?v={video_id}'
        logger.warning("No videos found")
        return None
    except Exception as e:
        logger.error(f"Error searching YouTube: {e}")
        return None

@app.route('/')
def index():
    logger.info("Serving index page")
    return render_template('index.html')

@app.route('/play')
def play():
    logger.info("Play endpoint called")
    band = get_random_band()
    video_url = search_youtube(band)
    logger.info(f"Returning band: {band}, video_url: {video_url}")
    return jsonify({'band': band, 'video_url': video_url})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/count')
def count_bands():
    try:
        with open('bands.csv', 'r', encoding='utf-8') as file:
            bands = file.readline().strip().split(',')
            bands = [band.strip() for band in bands if band.strip()]
            return jsonify({'total_bands': len(bands)})
    except Exception as e:
        logger.error(f"Error counting bands: {e}")
        return jsonify({'error': 'Error counting bands'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    logger.info(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port) 