FROM python:3.10-slim

WORKDIR /usr/src/
ARG DOWNLOAD_PATH=./app/src/U2Net/saved_models/u2net

COPY app ./app
COPY requirements.txt .
RUN apt-get update && apt-get install -y curl
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --no-cache -r requirements.txt
# RUN curl -L "https://www.dropbox.com/scl/fi/ktppzbrmddd6ti15tx49s/u2net.pth?dl=1" -o $DOWNLOAD_PATH/u2net.pth
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$PORT"]
