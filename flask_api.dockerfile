FROM python:3.7-alpine

RUN mkdir ./application
WORKDIR /application

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./flask_web_api ./
ENV FLASK_APP=flask_web_api
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

CMD ["flask", "run"]
