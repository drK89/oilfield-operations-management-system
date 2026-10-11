FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt && pip install -e .
RUN python seed_demo.py
CMD ["streamlit","run","dashboard.py","--server.address=0.0.0.0"]
