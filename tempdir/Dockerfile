FROM python
RUN pip install flask
RUN pip install requests
COPY ./templates /home/myapp/templates/
COPY ./referenceFiles /home/myapp/referenceFiles/
COPY flask-web-app.py /home/myapp/
COPY mapquestBackend.py /home/myapp/
EXPOSE 6060
CMD python /home/myapp/flask-web-app.py
