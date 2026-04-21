from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Lavu API", version="1.0.0")

# Allow frontend apps to access your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later to your frontend domain for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Lavu API is running 🔥"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
