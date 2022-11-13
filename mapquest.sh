#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static
mkdir tempdir/referenceFiles

cp flaskWebApp.py tempdir/.
cp mapquestBackend.py tempdir/.
cp testMapquest.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.
cp -r referenceFiles/* tempdir/referenceFiles/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install requests" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  ./referenceFiles /home/myapp/referenceFiles/" >> tempdir/Dockerfile
echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY  flaskWebApp.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY  mapquestBackend.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY  testMapquest.py /home/myapp/" >> tempdir/Dockerfile

echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/flaskWebApp.py" >> tempdir/Dockerfile

cd tempdir
docker build -t mapquestapp --no-cache .
docker run -t -d -p 5050:5050 --name mapquestapprunning mapquestapp
docker ps -a
