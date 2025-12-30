import requests

def fetch_playlists():
    url = "https://api.freeapi.app/api/v1/public/youtube/playlists"
    response = requests.get(url)
    result = response.json()

    if result.get("success"):
        playlists = result["data"]["data"]  # list of playlists

        for index, playlist in enumerate(playlists, start=1):
            snippet = playlist["snippet"]

            title = snippet["title"]
            description = snippet["description"]
            channel = snippet["channelTitle"]
            published = snippet["publishedAt"]

            print(f"{index}. {title}")
            print(f"   Channel    : {channel}")
            print(f"   Published  : {published}")
            print(f"   Description: {description[:80]}...")
            print("-" * 60)
    else:
        print("Failed to fetch playlists")

def main():
    fetch_playlists()

if __name__ == "__main__":
    main()
