FROM python:3.8.10

RUN mkdir -p /appfolder

COPY . /appfolder

RUN python3 -m pip install -r /appfolder/requirements.txt

EXPOSE 5000

CMD ["python","/appfolder/app.py"]

