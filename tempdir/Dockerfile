FROM python
RUN pip install flask
RUN pip install requests
COPY  ./templates /home/myapp/templates/
COPY  ./referenceFiles /home/myapp/referenceFiles/
COPY  ./static /home/myapp/static/
COPY  flaskWebApp.py /home/myapp/
COPY  mapquestBackend.py /home/myapp/
COPY  testMapquest.py /home/myapp/
EXPOSE 5050
CMD python3 /home/myapp/flaskWebApp.py
