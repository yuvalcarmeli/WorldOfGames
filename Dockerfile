FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN ls -la /app 
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run", "--host=0.0.0.0"]
