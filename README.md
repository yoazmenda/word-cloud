
# Flask Word Cloud Generator

## Introduction

This project is a Flask-based web application that allows users to generate word clouds from text input. The application features a simple web interface where users can enter text and receive a word cloud visualization as a result.

## Prerequisites

Before running this application, you will need:
- Python 3.6 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine using the following command:

```sh
git clone https://github.com/yoazmenda/word-cloud
```

Navigate into the project directory:

```sh
cd word-cloud
```

### 2. Virtual Environment Setup

It's recommended to use a virtual environment for Python projects to manage dependencies efficiently. To create and activate a virtual environment, follow these steps:

#### For Unix-like Systems (Linux/macOS):

Create a virtual environment:

```sh
python3 -m venv venv
```

Activate the virtual environment:

```sh
source venv/bin/activate
```

#### For Windows:

Create a virtual environment:

```cmd
python -m venv venv
```

Activate the virtual environment:

```cmd
.\venv\Scripts\activate
```

### 3. Install Dependencies

With the virtual environment activated, install the project dependencies:

```sh
pip install -r requirements.txt
```

### 4. Run the Flask Server

Finally, start the Flask server with the following command:

```sh
python app.py
```

The application will now be running on [http://localhost:5000](http://localhost:5000). Navigate to this URL in your web browser to use the application.

## Usage

- Go to [http://localhost:5000](http://localhost:5000) in your web browser.
- Enter text into the text box on the left side of the page.
- Click "Generate" to create the word cloud. The word cloud image will be displayed on the right side of the page.

## Closing the Application

To stop the Flask server, press `CTRL+C` in the terminal. If you wish to exit the virtual environment, type `deactivate`.