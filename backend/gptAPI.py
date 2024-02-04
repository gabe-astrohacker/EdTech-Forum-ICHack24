import requests
from youtube_transcript_api import YouTubeTranscriptApi

openai_api_key = "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"


def keywords_to_list(text):
    resp = (make_prompt(text + "\n\nCan you give me 20 keywords as academic topics and split them into single words")
            .split("1.", 1))
    output = "." + resp[1]
    suggestions = output.split('\n')
    new_suggestions = []
    for suggestion in suggestions:
        new_suggestion = suggestion.split('.', 1)
        new_suggestions.append(new_suggestion[1].strip())

    return new_suggestions


def summarise_video(video_id):
    transcript_as_dict = YouTubeTranscriptApi.get_transcript(video_id)

    open_ai_input = ""
    for entry in transcript_as_dict:
        open_ai_input = open_ai_input + entry["text"] + " "

    return make_prompt("Summarise this text in 100 words or less: " + open_ai_input)


def make_prompt(prompt):
    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print("Error:", response.status_code, response.text)
