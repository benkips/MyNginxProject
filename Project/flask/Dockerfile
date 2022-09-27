
# Step 1: Import the Os
FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Step 2: Install pip and Python Dependencies
RUN python3 --version
RUN pip3 --version
# Step 3: Create a Work Directory
WORKDIR /app

# Step 4: copy all Project Files
COPY . /app

# Step 5: Install all Dependencies for WSGI
RUN pip3 install --no-cache-dir -r requirements.txt

# Step 6:  run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
