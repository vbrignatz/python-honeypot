FROM python:3.9
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY realapp.py .
EXPOSE 8080
CMD ["uvicorn", "realapp:api", "--host", "0.0.0.0", "--port", "8080"]