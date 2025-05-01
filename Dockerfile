# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Set environment variables for Spotipy
ENV SPOTIPY_CLIENT_ID="your_client_id"
ENV SPOTIPY_CLIENT_SECRET="your_client_secret"

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]