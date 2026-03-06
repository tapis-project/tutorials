
FROM python:3.10

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY sentiment-analysis.py sentiment-analysis.py

RUN mkdir .cache
RUN chmod 777 -R .cache

ENTRYPOINT ["python3", "/sentiment-analysis.py"]




