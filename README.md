# bg_remover
Smart Image Background Remover (API-based tool)

Demo - https://clearback.netlify.app/
## Current state
Current version removes background using U2Net library and rough thresholding.
Still to do:

- Improve thresholding with advanced algorithms

- Add background customization

- Add user-friendly input for CLI version

- Create a proper UI in a seperate repo

- Experiment with alternative models


---

Note: The first Docker build may take several minutes as it downloads and installs large dependencies (e.g., PyTorch). Subsequent builds will be much faster.

---
## Table of Contents
  - [Current state](#current-state)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Installation](#installation)
      - [Windows:](#windows)
        - [Virtual environment](#virtual-environment)
        - [Docker:](#docker)
      - [Linux:](#linux)
        - [Virtual environment](#virtual-environment-1)
        - [Docker:](#docker-1)
  - [Usage](#usage)
      - [Windows:](#windows-2)
        - [Virtual environment](#virtual-environment-2)
        - [Docker:](#docker-2)
      - [Linux:](#linux-1)
        - [Virtual environment](#virtual-environment-3)
        - [Docker:](#docker-3)
  - [Other](#other)
  - [Reference](#reference)



---

## About

---
## Installation


### Windows:
#### Virtual environment
```bash
# Install Python 3.10 if needed
# On https://www.python.org/downloads/windows/, search for "Python 3.10.0" and download the Windows x64 installer listed just below that heading and run the installer

# Create virtual environment
py -3.10 -m venv .venv

# Activate virtual environment
.venv\Scripts\activate

# Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```
#### Docker
```bash
# Build the docker image and run the container
make all
```
### Linux:
#### Virtual environment
Compatible with Python versions 3.10 - 3.12

For pip: 
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
For uv:

```bash
# Create virtual environment
uv venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```
#### Docker
```bash
# Build the docker image and run the container
make all
```

---
## Usage

### Windows:
#### Virtual environment
```bash
# Activate virtual environment
.venv\Scripts\activate

# Run the server
uvicorn app.main:app --host 0.0.0.0 --port 8080

# Access the server at: http://localhost:8080/

# Test the POST API via the interactive docs: http://localhost:8080/docs
```
#### Docker
```bash
# Build the docker image and run the container
make all

# Additional commands are available in the Makefile (all are commented).
```

### Linux:
#### Virtual environment
```bash
# Activate virtual environment
source .venv/bin/activate

# Run the server
uvicorn app.main:app --host 0.0.0.0 --port 8080

# Access the server at: http://localhost:8080/ or http://0.0.0.0:8080/

# Test the POST API via the interactive docs: http://localhost:8080/docs
```
#### Docker
```bash
# Build the docker image and run the container
make all

# Additional commands are available in the Makefile (all are commented).
```

---
## Other

## Reference

Based on the original **U²-Net** implementation: [xuebinqin/U-2-Net](https://github.com/xuebinqin/U-2-Net)

