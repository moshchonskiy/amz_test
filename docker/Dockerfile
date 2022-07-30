FROM python:3.9.11-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update \
    && apt-get install -y apt-transport-https ca-certificates curl net-tools \
    && apt-get -y autoclean && apt-get -y autoremove \
    && rm -rf /var/lib/apt-get/lists/* /var/cache/apt

WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir -q -U -r /app/requirements.txt

CMD sh -c 'while sleep 3600; do :; done'