import requests
from youtube_transcript_api import YouTubeTranscriptApi
import gptAPI
from flask_cors import CORS
from flask import Flask, request, url_for

from backend.searchEngine import search
from databaseWrapper import *

app = Flask(__name__)
CORS(app)

@app.route('/resource_upload', methods=['POST'])
def resource_upload(link, description):
    response = requests.get(link)
    if response.status_code != 200:
        # TODO: ask user to re-enter
        print("Error uploading")
        return

    html_text = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'}).text

    website_text = gptAPI.html_to_text(html_text)
    resource_keywords = gptAPI.text_to_keywords(website_text)

    if description is None:
        description = gptAPI.summarise(website_text)

    add_resource(link, description, resource_keywords)


# AUTHENTICATION

@app.route('/sign_up', methods=['POST'])
def sign_up(email, password):
    create_user(email, password)


@app.route('/login', methods=['POST'])
def login(email, password):
    sign_in_user(email, password)


@app.route('/logout', methods=['POST'])
def logout():
    sign_out_user()


# RESOURCE FUNCTIONALITY
@app.route('/search_for', methods=['GET'])
def search_for(query):
    return [(link, get_resource_description(link)) for link in search(query)]


@app.route('/upvote', methods=['POST'])
def upvote(url):
    inc_rep(url, 'i')


@app.route('/downvote', methods=['POST'])
def downvote(url):
    dec_rep(url, 'i')


@app.route('/revert_upvote', methods=['POST'])
def revert_upvote(url):
    inc_rep(url, 'd')


@app.route('/revert_downvote', methods=['POST'])
def revert_downvote(url):
    dec_rep(url, 'd')


def transcribe_video(link):
    video_id = link  # TODO: turn link into video_id
    transcript_as_dict = YouTubeTranscriptApi.get_transcript(video_id)

    open_ai_input = ""
    for entry in transcript_as_dict:
        open_ai_input = open_ai_input + entry["text"] + " "

    return open_ai_input


if __name__ == '__main__':
    app.run(debug=True)