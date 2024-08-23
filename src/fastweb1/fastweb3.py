from fastapi import FastAPI, Depends, params
import uvicorn


#app = FastAPI()
def depfunc1():
    pass

def depfunc2():
    pass

app = FastAPI(dependencies=[Depends(depfunc1), Depends(depfunc2)])

# the dependency function:
def user_dep(name: str = params, password: str = params):
    return {"name": name, "valid": True}

# the dependency function:
def check_dep(name: str = params, password: str = params):
    if not name:
        raise


# the path function / web endpoint:
@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

# the path function / web endpoint:
@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True

if __name__ == "__main__":
    uvicorn.run("fastweb3:app")