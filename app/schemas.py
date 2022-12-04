from datetime import datetime

from pydantic import BaseModel, Field


class PrimeResponse(BaseModel):
    is_prime: bool = Field(..., alias="isPrime")


class TimeResponse(BaseModel):
    current_time: datetime = Field(..., alias="currentTime")


class APIKeyResponse(BaseModel):
    api_key: str = Field(..., alias="apiKey")
