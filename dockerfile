FROM --platform=linux/amd64 ghcr.io/owl-corp/python-poetry-base:3.12-slim

# Install project dependencies
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install

# Copy the source code in last to optimize rebuilding the image
COPY . .

EXPOSE 8000

ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "is_even:app", "--host", "0.0.0.0", "--port", "8000"]
