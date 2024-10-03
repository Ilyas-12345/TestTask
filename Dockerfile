FROM python:3.12

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

COPY . .

RUN chmod a+x /fastapi_app/Docker/app.sh
