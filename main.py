from fastapi import FastAPI 

app = FastAPI() 

@app.get("/home")
def home():
    return {"message":"Prince APi"}

#About Page

@app.get("/about")
def about():
    return {"Message":"About Page"}

#User

@app.get("/user")
def user():
    return {
        "User": ["Rohan", "Mohan","Ram"]
    }