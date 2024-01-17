# URL Shortener API

This is a simple URL shortener API implemented in Python using Flask. The API takes a long URL as input and returns a shortened version of the URL.

## Installation

Before running the project, make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navigate to the project directory:

   ```bash
   cd nome-do-repositorio
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```bash
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. The application will start running on `http://127.0.0.1:5000/` by default.

3. Use the following endpoints to interact with the API:

   - **Shorten URL:** Send a POST request to `http://127.0.0.1:5000/` with JSON data containing the original URL:

     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"url": "https://www.example.com"}' http://127.0.0.1:5000/
     ```

     The response will contain the shortened URL.

   - **Redirect to Original URL:** Access the shortened URL in your browser or use curl:

     ```bash
     curl http://127.0.0.1:5000/<short_code>
     ```

## Explanation

- The `encurtar_url` function generates an MD5 hash of the original URL and uses the first 8 characters as the short code.
- The Flask application has two routes:
  - `/` handles the URL shortening process, accepting POST requests with a JSON payload containing the original URL.
  - `/<short_code>` redirects to the original URL based on the provided short code.

Feel free to explore and modify the code according to your needs. If you encounter any issues or have suggestions, please create an issue in the repository.
