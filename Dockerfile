FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN python
RUN import nltk

COPY . .

CMD [ "python", "./scrape.py" ]
