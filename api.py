from fastapi import FastAPI, HTTPException
import logging
from connect_apis import (
    connect_openai,
    connect_serpapi,
    connect_shopify,
    connect_youtube,
    connect_ai_studio,
    connect_gemini
)

app = FastAPI()

@app.get("/connect/openai")
async def api_connect_openai():
    try:
        connect_openai()
        return {"message": "OpenAI connection tested successfully."}
    except Exception as e:
        logging.error(f"Error in OpenAI connection: {e}")
        raise HTTPException(status_code=500, detail="Error connecting to OpenAI")

@app.get("/connect/serpapi")
async def api_connect_serpapi():
    try:
        connect_serpapi()
        return {"message": "SerpAPI connection tested successfully."}
    except Exception as e:
        logging.error(f"Error in SerpAPI connection: {e}")
        raise HTTPException(status_code=500, detail="Error connecting to SerpAPI")

@app.get("/connect/shopify")
async def api_connect_shopify():
    try:
        connect_shopify()
        return {"message": "Shopify connection tested successfully."}
    except Exception as e:
        logging.error(f"Error in Shopify connection: {e}")
        raise HTTPException(status_code=500, detail="Error connecting to Shopify")

@app.get("/connect/youtube")
async def api_connect_youtube():
    try:
        connect_youtube()
        return {"message": "YouTube connection tested successfully."}
    except Exception as e:
        logging.error(f"Error in YouTube connection: {e}")
        raise HTTPException(status_code=500, detail="Error connecting to YouTube")

@app.get("/connect/ai_studio")
async def api_connect_ai_studio():
    try:
        connect_ai_studio()
        return {"message": "Google AI Studio connection tested successfully."}
    except Exception as e:
        logging.error(f"Error in Google AI Studio connection: {e}")
        raise HTTPException(status_code=500, detail="Error connecting to Google AI Studio")

@app.get("/connect/gemini")
async def api_connect_gemini():
    try:
        connect_gemini()
        return {"message": "Google Gemini connection tested successfully."}
    except Exception as e:
        logging.error(f"Error in Google Gemini connection: {e}")
        raise HTTPException(status_code=500, detail="Error connecting to Google Gemini")