FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /home/ubuntu/actions-runner/_work/buh-control/buh-control

COPY . .

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt 
