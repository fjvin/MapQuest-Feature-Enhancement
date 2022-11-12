FROM python
RUN pip install install flask
COPY ./templates /home/myapp/templates/
COPY ./referenceFiles /home/myapp/referenceFiles/
COPY flask-web-app.py /home/myapp/
COPY mapquestBackend.py /home/myapp/
EXPOSE 8080
CMD python3 /home/myapp/flask-web-app.py
