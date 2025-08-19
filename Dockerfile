FROM python:3.12-slim 
WORKDIR /src
COPY /src .
EXPOSE 8000
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
CMD ["fastapi", "dev", "main.py"]