FROM python:3.11
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN ln -s /usr/local/bin/streamlit /usr/bin/streamlit
EXPOSE 8501
CMD ["streamlit","run","app.py","--server.port=8501","--server.enableCORS=false"]