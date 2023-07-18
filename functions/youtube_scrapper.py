from streamlit_player import st_player
import youtube_dl
import urllib.request
import requests
import unicodedata
import re

# def download_videos(url):
#     ydl_opts = {
#         'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
#         'outtmpl': '%(title)s.%(ext)s',
#     }

#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
def youtube_scrapper(top_10):
    search_string = unicodedata.normalize('NFKD', top_10).encode('ascii', 'ignore').decode()
    youtube_str = re.sub("[ ]", "+", search_string)
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + youtube_str + '+trailer')
    vid_id = re.findall(r'watch\?v=(\S{11})', html.read().decode())

# Example usage
# video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
video_url ='https://www.youtube.com/watch?v=' #+ vid_id[0]
# download_videos(video_url)
st_player(video_url)