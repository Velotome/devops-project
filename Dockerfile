FROM python:3.12-slim 
WORKDIR /src
COPY /src .
CMD ["python", "__init__.py"]