
# Step 1: Import the Os
FROM alpine:latest

# Step 2: Install pip and Python Dependencies
RUN apk add --no-cache python3-dev
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
# Step 3: Create a Work Directory
WORKDIR /app

# Step 4: copy all Project Files
COPY . /app

# Step 5: Install all Dependencies for WSGI
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip3 --no-cache-dir install -r requirements.txt; \
	apk del .build-deps;

# Step 6:  run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
