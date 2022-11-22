FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
WORKDIR /usr/src/app/ImagesDRF
COPY ./requirements.txt /usr/src/app/ImagesDRF/requirements.txt
RUN pip install -r /usr/src/app/ImagesDRF/requirements.txt
COPY . /usr/src/app/ImagesDRF
EXPOSE 8000
