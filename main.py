from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is awesome",
        "content": "This framework is really easy to use and super fast",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is greate for we development",
        "content": "Python is a great language for web development",
        "date_posted": "April 21, 2025",
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts
