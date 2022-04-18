# syntax=docker/dockerfile:1
FROM python:3.8
ENV SRC_DIR /client
COPY src/* ${SRC_DIR}/
WORKDIR ${SRC_DIR}
ENV PYTHONUNBUFFERED=1
CMD ["python", "client.py"]