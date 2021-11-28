FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

ENTRYPOINT [ "python", "app.py" ]