import os
import httpx
from dotenv import load_dotenv
from typing import Any, Dict, Optional

load_dotenv()

class BeaNipaClient:
    """Shared HTTP client for the BEA API, narrowed down to just the NIPA tables"""

    BEA_API_URL = "https://apps.bea.gov/api/data"

    def __init__(self, timeout: float = 30.0):
        self.client = httpx.AsyncClient(
            timeout=timeout, headers={"Content-Type": "application/json"}
        )

    async def get(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a HTTP GET request to the API with unified error handling"""
        try:
            if params:
                params["userID"] = f"{os.getenv('API_KEY')}"
            response = await self.client.request("GET", self.BEA_API_URL, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_detail = f"HTTP {e.response.status_code}: {e.response.text}"
            raise Exception(f"API request failed: {error_detail}") from e
        except httpx.RequestError as e:
            raise Exception(f"Request error: {str(e)}") from e

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.client.aclose()