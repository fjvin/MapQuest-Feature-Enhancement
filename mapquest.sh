#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/referenceFiles

cp flask-web-app.py tempdir/.
cp mapquestBackend.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r referenceFiles/* tempdir/referenceFiles/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install install flask" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY ./referenceFiles /home/myapp/referenceFiles/" >> tempdir/Dockerfile
echo "COPY flask-web-app.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY mapquestBackend.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/flask-web-app.py" >> tempdir/Dockerfile

cd tempdir
docker build -t mapquestapp .
docker run -t -d -p 8080:8080 --name mapquestapprunning mapquestapp
docker ps -a
