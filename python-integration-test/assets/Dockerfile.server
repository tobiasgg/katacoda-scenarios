# syntax=docker/dockerfile:1
FROM python:3.8
ENV SRC_DIR /server
COPY src/* ${SRC_DIR}/
WORKDIR ${SRC_DIR}
ENV PYTHONUNBUFFERED=1
CMD ["python", "simple_webserver.py"]