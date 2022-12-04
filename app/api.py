from fastapi import APIRouter, Path, UploadFile, Response, HTTPException
from schemas import PrimeResponse, TimeResponse, APIKeyResponse
from prime import deterministic_miller_rabin_primality_test
from invert import invert
from datetime import datetime
import settings


api_router = APIRouter()


@api_router.get("/prime/{number}", response_model=PrimeResponse)
def is_prime(number: int = Path(title="Number to check", ge=1, le=9223372036854775807)):
    return PrimeResponse(isPrime=deterministic_miller_rabin_primality_test(number))


@api_router.post("/picture/invert")
async def invert_picture(picture: UploadFile):
    content_type = picture.content_type
    picture_bytes = await picture.read()
    inverted_picture = invert(picture_bytes, content_type)
    if not inverted_picture:
        raise HTTPException(status_code=400, detail="Image is larger than 12Mpx")
    return Response(content=inverted_picture, media_type=content_type)


@api_router.get("/time", response_model=TimeResponse)
def get_time(api_key: str = ""):
    if api_key != settings.PUBLIC_API_KEY:
        raise HTTPException(status_code=403, detail="Wrong API key provided")
    return TimeResponse(currentTime=datetime.utcnow())


@api_router.get("/api_key", response_model=APIKeyResponse)
async def get_api_key():
    return APIKeyResponse(apiKey=settings.PUBLIC_API_KEY)
