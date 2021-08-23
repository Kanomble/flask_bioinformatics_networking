FROM ubuntu:focal
MAINTAINER lukas.becker@hhu.de

RUN mkdir ./application
WORKDIR /application

ENV DEBIAN_FRONTEND noninteractive
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3-pip python3-dev && rm -rf /var/lib/apt/lists/*

RUN apt-get update && (apt-get install -t buster-backports -y mafft || apt-get install -y mafft) \
 && (apt-get install -t buster-backports -y fasttree || apt-get install -y fasttree) \
 && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./flask_mafft_fasttree ./
ENV FLASK_APP=flask_mafft_fasttree
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5001

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
