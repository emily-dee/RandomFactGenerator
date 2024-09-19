FROM python:3.11
WORKDIR /code
COPY main.py /code/
CMD ["python3", "main.py"]