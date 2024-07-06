from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import evaluation, health, auth
from .utils.cache import init_cache
from .utils.rate_limiter import init_rate_limiter

app = FastAPI()

# Initialize cache
init_cache()

# Initialize rate limiter
init_rate_limiter(app)

# Include routers
app.include_router(evaluation.router)
app.include_router(health.router)
app.include_router(auth.router)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Multimodal Evaluation and Comparison System API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
