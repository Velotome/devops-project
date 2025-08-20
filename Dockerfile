FROM python:3.12-slim AS devops-project
WORKDIR /src
COPY /src .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
CMD ["fastapi", "dev", "main.py"]

FROM python:3.12-slim AS devops-project-test
WORKDIR /src
COPY /src .
WORKDIR /tests
COPY /tests .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
CMD ["pytest"]