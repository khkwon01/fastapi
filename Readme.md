## 1. install virtural environment

- python3 -m venv venv

## 2. Activate environment

- source venv/bin/activate    (<-> deactivate)

## 3. Install essenital packages

- pip install fastapi unicorn ruff

## 4. 기본 fastapi 구성
```
from contextlib import asynccontextmanager
from fastapi import FastAPI, Query, Response, status
from models import load_image_model

models = {}
@asynccontextmanager
def lifespan(app: FastAPI):
    models["text2image"] = load_image_model()

    models.clear()
    
app = FastAPI(lifespan=lifespan)
@app.get(
    "/generate/test",
    responses={status.HTTP_200_OK: {"content": {"image/png": {}}}},
    response_class=Response,
)
def test():
    pass
```
