# This is the dockerfile to run and package the PageSage webapp
FROM python:3.6-alpine
MAINTAINER boxoforanmore
ADD . .
RUN pip install -r ./requirements.txt \
    && export FLASK_APP='page-sage.py'

ENV OAUTHLIB_INSECURE_TRANSPORT=1
ENV OAUTHLIB_RELAX_TOKEN_SCOPE=2

ENTRYPOINT ["python"]

CMD ["page-sage.py"]
