FROM python:3.12

WORKDIR /app

COPY ./app /app/app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

ENTRYPOINT ["python", "-m", "uvicorn"]

# Run the FastAPI app using uvicorn
CMD ["app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
