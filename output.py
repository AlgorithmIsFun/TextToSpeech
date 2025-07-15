import requests

response = requests.get(
    "http://localhost:5002/process",
    params={
	#Add Text to Speech here
        "INPUT_TEXT": "Hello world. Testing 1 2 3 4.",
        "INPUT_TYPE": "TEXT",
        "LOCALE": "en_US",
        "VOICE": "p376",
        "OUTPUT_TYPE": "AUDIO",
        "AUDIO": "WAVE_FILE"
    }
)

if response.ok:
    with open("output.wav", "wb") as f:
        f.write(response.content)
    print("Saved speech to output.wav")
else:
    print("Error:", response.status_code, response.text)
