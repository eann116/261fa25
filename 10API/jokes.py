import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    setup = data["setup"]
    punchline = data["punchline"]

    return setup, punchline

if __name__ == "__main__":
    setup, punchline = get_random_joke()
    print(setup)
    input("Press Enter for the punchline...")
    print(punchline)
