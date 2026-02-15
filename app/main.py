from fastapi import FastAPI
from app.api.health import router as health_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version="0.1.0")
app.include_router(health_router, prefix="/api")


@app.get("/")
def root():
    return {"message": f"{settings.PROJECT_NAME} is running"}


if __name__ == "__main__":
    try:
        import uvicorn

        uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
    except Exception:
        print("uvicorn not available. Run the app with: uvicorn app.main:app --reload")
