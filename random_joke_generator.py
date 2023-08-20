import requests

def fetch_random_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data.get("setup"), joke_data.get("punchline")
    else:
        return None, None

if __name__ == "__main__":
    print("Random Joke Generator")
    input("Press Enter to fetch and display a random joke...")
    
    setup, punchline = fetch_random_joke()

    if setup and punchline:
        print("Joke:")
        print(setup)
        input("Press Enter to reveal the punchline...")
        print(punchline)
    else:
        print("Failed to fetch a joke. Please try again later.")
