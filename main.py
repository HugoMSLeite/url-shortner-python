from flask import Flask, redirect, render_template, request
import hashlib

app = Flask(__name__)

# Dictionary to store URL mappings
url_mapping = {}


def encurtar_url(url_original):
    # Gerar hash MD5 da URL original
    md5_hash = hashlib.md5(url_original.encode()).hexdigest()

    # Utilizar os primeiros 8 caracteres do hash como URL encurtada
    url_encurtada = md5_hash[:8]

    return url_encurtada


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.json["url"]
        print(original_url)
        short_code = encurtar_url(original_url)
        url_mapping[short_code] = original_url
        short_url = request.host_url + short_code
        return {"shortUrl": short_url}
    return render_template('index.html')


@app.route('/<short_code>')
def redirect_to_original_url(short_code):
    if short_code in url_mapping:
        original_url = url_mapping[short_code]
        return redirect(original_url)
    else:
        return "Short URL not found."


if __name__ == '__main__':
    app.run(debug=True)
