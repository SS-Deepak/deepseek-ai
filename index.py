import random
import requests
import json
import time

url = 'http://localhost:11434/api/generate'

data = {
    "model": "deepseek-r1:7b",
    "prompt": "Provide list of customer mock data, including name, age, address, county, vecle, in a few words",
    "system": "Provide the short and consise output",
    "max_tokens": 150
}

loading_phrases = [
    'Thinking...',
    'Structuring query...',
    'Phrasing answer...',
    'Optimizing...',
    'Modeling words...',
    'Ready...',
    'Evaluating...'
]


loading = True

i = 0

response = requests.post(url, json=data, stream=True)

while (loading):
    if response.status_code == 200:
        loading = False
    if response.status_code and response.status_code != 200:
        print(response.text, 'Error')
        loading = False

    print(random.choice(loading_phrases))
    time.sleep(3)

    i += 1


if response.status_code == 200:
    loading = False
    print('Generating text: ', flush=True)
    for line in response.iter_lines():
        if line:
            decode_line = line.decode("utf-8")
            result = json.loads(decode_line)

            generated_text = result.get("response", "")
            print(generated_text, end="", flush=True)
else:
    loading = False
    print("Error: ", response.text)
