import requests


url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize'

headers = {'accept': 'audio/wav'}

r = requests.get(
    url, 
    params={"text": "Internet of Things and Watson API is Awesome"},
    auth=('xxxxx-f3c0-46e6-b731-xxxxxx', 
          '7r4RMxxxxx'), 
    headers=headers)

with open('sound.wav', 'wb') as fd:
    for chunk in r.iter_content(1024):
        fd.write(chunk)
