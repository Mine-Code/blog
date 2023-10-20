FROM python:3.10

WORKDIR /app
COPY . .

RUN apt-get install default-libmysqlclient-dev

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "manage.py", "upgrade"]
