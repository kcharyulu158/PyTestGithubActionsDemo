# 1. Use an official lightweight Python image
FROM python:3.11-slim

# 2. Install essential system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# 3. Download and install Google Chrome Stable directly via the official .deb package
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get update \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && rm -rf /var/lib/apt/lists/*

# 4. Set the working directory inside the container
WORKDIR /app

# 5. Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the project files into the container
COPY . .

# 7. Command to execute the pytest suite when the container starts
CMD ["python", "-m", "pytest"]
