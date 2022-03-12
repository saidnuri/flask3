from flask import Flask,request
from pytube import YouTube
from youtubesearchpython import VideosSearch
import json

app = Flask(__name__)


@app.route('/<string:name>')
def index(name:str):
    yt = YouTube('http://youtube.com/watch?v='+str(name))
    file=yt.streams.filter(only_audio=True).first().url
    return file
@app.route('/snc/<string:search>')
def snc(search:str):
    videosSearch = VideosSearch(search, limit = 50)
    dict=videosSearch.result()
    den=json.dumps(dict,indent=1)
    return den

if __name__ == '__main__':
    app.run()
