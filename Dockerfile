FROM public.ecr.aws/lambda/python:3.8

RUN pip install tweepy
RUN pip install Pillow -t .

COPY random_needle.py ./
COPY needle_drawer.py ./
COPY secrets.py ./
COPY twitter_accessor.py ./
COPY tweet_builder.py ./
COPY app.py ./


CMD ["app.handler"]
