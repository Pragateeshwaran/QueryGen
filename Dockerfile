# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app

# Expose the port that Streamlit uses (8501 by default)
EXPOSE 8501

# Set the command to run Streamlit
CMD ["streamlit", "run", "app.py"]
