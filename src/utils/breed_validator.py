import os
import httpx

from typing import List
from dotenv import load_dotenv

load_dotenv()
CAT_API_URL = os.getenv("CAT_API_URL")
CAT_BREEDS: List[str] = []


async def fetch_breeds():
    """Fetch breed names from The Cat API."""
    global CAT_BREEDS
    if not CAT_BREEDS:
        async with httpx.AsyncClient() as client:
            response = await client.get(CAT_API_URL)
            response.raise_for_status()
            breeds = response.json()
            CAT_BREEDS = [breed["name"] for breed in breeds]
    return CAT_BREEDS
