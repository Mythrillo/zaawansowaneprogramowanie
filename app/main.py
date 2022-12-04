import settings  # noqa: F401
from api import api_router
from fastapi import FastAPI

app = FastAPI(
    title="Zaawansowane Programowanie 2022/2023",
    description="Uni course",
    contact={"name": "Mikołaj Kałuża", "email": "mikolaj.kaluza1@edu.uekat.pl"},
)
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
