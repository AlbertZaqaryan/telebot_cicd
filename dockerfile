FROM python:3.12

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY . /app/

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]

