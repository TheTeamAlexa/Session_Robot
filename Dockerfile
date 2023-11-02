FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt
CMD ["python3", "bot.py"]
