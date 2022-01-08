from flask import Flask,request
from pytube import YouTube

app = Flask(__name__)


@app.route('/<string:name>')
def index(name:str):
    yt = YouTube('http://youtube.com/watch?v='+str(name))
    file=yt.streams.filter(only_audio=True).first().url
    return file

if __name__ == '__main__':
    app.run()
