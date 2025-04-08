# Use the slim Python 3.10 image as a base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies, including git and build tools
RUN apt-get update && \
    apt-get install -y git gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
    


# Copy requirements file first to leverage Docker cache
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the project files to the container
COPY . .

# Expose the port if needed (optional)
EXPOSE 8501

# Command to run the Streamlit app (or your main app)
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

