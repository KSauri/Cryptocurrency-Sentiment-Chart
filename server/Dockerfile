FROM python:3.6
EXPOSE 5000/tcp
ADD requirements.txt /server/
ADD . /server
VOLUME ${pwd}/server.py:/server/server.py
WORKDIR /server
RUN pip install -r requirements.txt
ENV SECRET_KEY=${SECRET_KEY}

ENTRYPOINT ["python"]
CMD ["server.py"]
