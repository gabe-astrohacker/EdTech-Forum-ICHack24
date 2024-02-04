from databaseWrapper import create_user, add_resource
import requests
from youtube_transcript_api import YouTubeTranscriptApi
import gptAPI


def resource_upload(user_id, name, link, description):
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


def transcribe_video(link):
    video_id = link  # TODO: turn link into video_id
    transcript_as_dict = YouTubeTranscriptApi.get_transcript(video_id)

    open_ai_input = ""
    for entry in transcript_as_dict:
        open_ai_input = open_ai_input + entry["text"] + " "

    return open_ai_input


