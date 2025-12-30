import requests

def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        jokes_list = data["data"]["data"]  # list of jokes
        
        for joke in jokes_list:
            print(f"ID: {joke['id']}")
            print(f"Joke: {joke['content']}")
            print(f"Categories: {joke['categories']}")
            print("-" * 50)
    else:
        raise Exception("Failed to fetch jokes")

def main():
    try:
        fetch_random_jokes()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()























