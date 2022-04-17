from flask import Flask
from pytube import YouTube
from youtubesearchpython import VideosSearch
import json
import youtube_dl
import os
from flask import send_from_directory
app = Flask(__name__)


@app.route('/<string:name>')
def index(name:str):
    ydl = youtube_dl.YoutubeDL()
    # Add all the available extractors
    ydl.add_default_info_extractors()

    result = ydl.extract_info('https://www.youtube.com/watch?v='+str(name)
                              , download=False  # We just want to extract the info
                              )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        Video = result['entries'][0]
    else:
        # Just a video
        video = result

        for i in (video["formats"]):
            if (i['ext'] == 'm4a'):
                link = (i["url"])
                break
    return link

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route('/snc/<string:search>')
def snc(search:str):
    videosSearch = VideosSearch(search, limit = 50)
    dict=videosSearch.result()
    den=json.dumps(dict,indent=1)
    return den
@app.route('/ytb_video/<string:id>')
def get_video(id:str):
    yt = YouTube('http://youtube.com/watch?v='+str(id))
    linker = {"Linkler": [yt.streams.get_highest_resolution().url, yt.streams.get_lowest_resolution().url],
              "kaliteler:": [yt.streams.get_highest_resolution().resolution,
                             yt.streams.get_lowest_resolution().resolution]}

    return linker

if __name__ == '__main__':
    app.run()