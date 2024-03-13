from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/does_it_work/')
def some_route():
    return 'working'


if __name__ == '__main__':
    uvicorn.run('main:app', port=5000)
