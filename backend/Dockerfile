FROM python:3.11.5

WORKDIR /hexocean

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt && \
    pip install -r requirements_dev.txt

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["/entrypoint.sh", "development"]

HEALTHCHECK --interval=5m --timeout=15s \
    CMD curl -f http://0.0.0.0:8000/api || exit 1
