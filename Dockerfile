FROM python:3.12-slim 
WORKDIR /src
COPY /src .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "__init__.py"]