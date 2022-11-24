FROM python:3.9.10-slim-buster
COPY . /usr/app/
ENV LISTEN_PORT=3000
EXPOSE 3000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python app.py