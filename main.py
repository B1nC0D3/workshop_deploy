from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def some_route():
    return 'working'
