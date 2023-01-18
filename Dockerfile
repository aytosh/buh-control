
FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /home/devops/actions-runner/_work/tutor-USA/tutor-USA

COPY . .

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt 
