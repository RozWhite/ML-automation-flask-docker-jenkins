FROM python:3.9.10-slim-buster
COPY app.py /usr/app/
COPY iris.py /usr/app/
COPY requirements.txt /usr/app/
COPY lg.pkl /usr/app/
ENV LISTEN_PORT=3000
EXPOSE 3000
WORKDIR /usr/app/

RUN pip install -r requirements.txt
CMD python app.py