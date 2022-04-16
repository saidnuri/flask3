from flask import Flask,request
from pytube import YouTube
from youtubesearchpython import VideosSearch
import json

app = Flask(__name__)


@app.route('/')
def index(name:str):
     return "selam"
@app.route('/snc/<string:search>')
def snc(search:str):
    videosSearch = VideosSearch(search, limit = 50)
    dict=videosSearch.result()
    den=json.dumps(dict,indent=1)
    return den


if __name__ == '__main__':
    app.run()
