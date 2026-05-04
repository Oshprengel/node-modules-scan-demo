import yaml
from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/load')
def load_config():
    raw = request.args.get('config', '')
    return yaml.load(raw)


@app.route('/fetch')
def fetch_url():
    url = request.args.get('url', '')
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
