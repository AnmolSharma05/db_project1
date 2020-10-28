FROM python:3

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    gettext

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --default-timeout=200 -r /requirements.txt \
    && rm -rf /requirements.txt

COPY ./entrypoint.sh /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./start-django.sh /start-django
RUN sed -i 's/\r$//g' /start-django
RUN chmod +x /start-django

COPY . /app

COPY config/nginx/default /etc/nginx/sites-available/default
COPY config/nginx/nginx.conf /etc/nginx/nginx.conf

WORKDIR /app

EXPOSE 80/tcp 443/tcp

ENTRYPOINT ["/entrypoint"]

CMD ["sh" , "/start-django"]
