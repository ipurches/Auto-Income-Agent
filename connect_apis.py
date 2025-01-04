import os
import openai
import requests
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up API keys from environment variables
API_KEYS = {
    "openai": os.getenv("OPENAI_API_KEY"),
    "serpapi": os.getenv("SERPAPI_API_KEY"),
    "shopify": os.getenv("SHOPIFY_API_KEY"),
    "shopify_store": os.getenv("SHOPIFY_STORE_URL"),
    "youtube": os.getenv("YOUTUBE_API_KEY"),
    "ai_studio": os.getenv("AI_STUDIO_API_KEY"),
    "gemini": os.getenv("GEMINI_API_KEY")
}

# 1. OpenAI API
def connect_openai():
    openai.api_key = API_KEYS["openai"]
    if not openai.api_key:
        logging.error("OPENAI_API_KEY is missing.")
        return
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Test OpenAI connection"}],
            max_tokens=5
        )
        if response.choices:
            logging.info(f"OpenAI connection successful: {response.choices[0]['message']['content'].strip()}")
        else:
            logging.error("OpenAI did not return any choices.")
    except Exception as e:
        logging.error(f"Error connecting to OpenAI: {e}")

# 2. SerpAPI
def connect_serpapi():
    serpapi_key = API_KEYS["serpapi"]
    if not serpapi_key:
        logging.error("SERPAPI_API_KEY is missing.")
        return
    try:
        params = {"q": "test", "api_key": serpapi_key}
        response = requests.get("https://serpapi.com/search", params=params)
        response.raise_for_status()
        data = response.json()
        if "search_metadata" in data and data["search_metadata"]["status"] == "Success":
            logging.info(f"SerpAPI connection successful: {data['search_metadata']['status']}")
        else:
            logging.error(f"Error connecting to SerpAPI: {data}")
    except Exception as e:
        logging.error(f"Error connecting to SerpAPI: {e}")

# 3. Shopify API
def connect_shopify():
    shopify_key = API_KEYS["shopify"]
    store_url = API_KEYS["shopify_store"]
    if not shopify_key or not store_url:
        logging.error("SHOPIFY_API_KEY or SHOPIFY_STORE_URL is missing.")
        return
    try:
        headers = {"X-Shopify-Access-Token": shopify_key}
        response = requests.get(f"{store_url}/admin/api/2023-01/shop.json", headers=headers)
        response.raise_for_status()
        shop_data = response.json()
        if 'shop' in shop_data:
            logging.info(f"Shopify connection successful: {shop_data['shop']['name']}")
        else:
            logging.error(f"Error connecting to Shopify: {shop_data}")
    except Exception as e:
        logging.error(f"Error connecting to Shopify: {e}")

# 4. YouTube API
def connect_youtube():
    youtube_key = API_KEYS["youtube"]
    if not youtube_key:
        logging.error("YOUTUBE_API_KEY is missing.")
        return
    try:
        response = requests.get(
            "https://www.googleapis.com/youtube/v3/channels",
            params={"part": "snippet", "id": "UC_x5XG1OV2P6uZZ5FSM9Ttw", "key": youtube_key}
        )
        response.raise_for_status()
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            logging.info(f"YouTube connection successful: {data['items'][0]['snippet']['title']}")
        else:
            logging.warning("YouTube connection successful, but no data was returned.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error connecting to YouTube: {e}")

# 5. Google AI Studio API
def connect_ai_studio():
    ai_studio_key = API_KEYS["ai_studio"]
    ai_studio_url = os.getenv("AI_STUDIO_URL")
    if not ai_studio_key or not ai_studio_url:
        logging.error("AI_STUDIO_API_KEY or AI_STUDIO_URL is missing.")
        return
    try:
        response = requests.get(
            ai_studio_url,
            headers={"Authorization": f"Bearer {ai_studio_key}"}
        )
        response.raise_for_status()
        data = response.json()
        logging.info("Google AI Studio connection successful.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error connecting to Google AI Studio: {e}")

# 6. Google Gemini API
def connect_gemini():
    gemini_key = API_KEYS["gemini"]
    if not gemini_key:
        logging.error("GEMINI_API_KEY is missing.")
        return
    try:
        response = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent",
            headers={"Content-Type": "application/json"},
            params={"key": gemini_key},
            json={
                "contents": [
                    {
                        "parts": [{"text": "Explain how AI works"}]
                    }
                ]
            }
        )
        response.raise_for_status()
        data = response.json()
        logging.info(f"Google Gemini connection successful: {data}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error connecting to Google Gemini: {e}")

if __name__ == "__main__":
    logging.info("Connecting to APIs...")
    connect_openai()
    connect_serpapi()
    connect_shopify()
    connect_youtube()
    connect_ai_studio()
    connect_gemini()
    logging.info("All API connections tested.")
