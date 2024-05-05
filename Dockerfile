
FROM python:3.9
 
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./Makefile /code/Makefile
COPY ./setup.sh /code/setup.sh
RUN pip install -q --no-cache-dir --upgrade -r /code/requirements.txt
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]