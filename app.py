from flask import Flask, request
import platform
import encoder
import gc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def route():
    if request.method == 'POST':
        print(request.form['text'])
        music_name = encoder.getMusic(request.form['text'])
        return music_name
    return str(gc.collect())


@app.after_request
def after_request(response):
    allowed_origins = ['http://127.0.0.1:5500', 'https://it-engineer-k.github.io']
    origin = request.headers.get('Origin')
    if origin in allowed_origins:
        response.headers.add('Access-Control-Allow-Origin', origin)
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

