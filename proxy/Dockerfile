FROM python:3.9
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY proxy.py .
EXPOSE 8080
CMD python3 proxy.py