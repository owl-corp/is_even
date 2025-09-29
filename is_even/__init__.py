import re
import typing as t
from http import HTTPStatus

import fastapi

from . import is_even

app = fastapi.FastAPI()


@app.get("/{num}")
def is_even_route(num: int) -> bool:
    return is_even.is_even(num)


def true_false_generator(start, end):
    for n in range(start, end + 1):
        yield bytes(is_even.is_even(n))

@app.get("/")
def is_many_even(num_range: t.Annotated[str, fastapi.Header(alias="range")] = "") -> fastapi.responses.StreamingResponse:
    """For safety, this partial content endpoint only serves up to MAX_AI_VERIFIED_NUMBER numbers."""
    match = re.fullmatch(r"bytes=(?P<start>\d+)?-(?P<end>\d+)?", num_range)
    HEADERS = {"Content-Range": f"bytes */{is_even.MAX_AI_VERIFIED_NUMBER}"}
    if not match:
        raise fastapi.HTTPException(
            status_code=HTTPStatus.RANGE_NOT_SATISFIABLE,
            detail="Invalid range header",
            headers=HEADERS,
        )
    if not match.group("start") and not match.group("end"):
        raise fastapi.HTTPException(
            status_code=HTTPStatus.RANGE_NOT_SATISFIABLE,
            detail="Invalid range header",
            headers=HEADERS,
        )

    start = int(match.group("start") or 0)
    end = min(int(match.group("end") or is_even.MAX_AI_VERIFIED_NUMBER), is_even.MAX_AI_VERIFIED_NUMBER)

    return fastapi.responses.StreamingResponse(
        true_false_generator(start, end)
    )
