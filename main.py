from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def some_route():
    return 'working'


if __name__ == '__main__':
    uvicorn.run('main:app', port=5000)
