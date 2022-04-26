# In path/to/your/dev/folder/Dockerfile
# Base Image
FROM python:3.10.0

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD TCP_Server.py /

EXPOSE 5000

CMD ["python", "./TCP_Server.py"]