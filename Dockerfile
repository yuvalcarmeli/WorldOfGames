FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt MainScores.py Utils.py /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
