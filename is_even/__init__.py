import fastapi

from . import is_even

app = fastapi.FastAPI()

@app.get("/{num}")
def is_even_route(num: int) -> bool:
    return is_even.is_even(num)