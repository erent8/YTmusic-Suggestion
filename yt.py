from googleapiclient.discovery import build
import random
import os

# Add your YouTube Data API key here
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'
RECOMMENDED_SONGS_FILE = 'youtube_recommended_songs.txt'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def fetch_from_youtube_api(query, max_results=10):
    """
    Fetches search results from the YouTube Data API.
    
    :param query: Search term (e.g., "popular music")
    :param max_results: Maximum number of results to return
    :return: A list of song information
    """
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    return response.get('items', [])

def load_recommended_songs():
    """Loads previously recommended songs from a file."""
    if os.path.exists(RECOMMENDED_SONGS_FILE):
        with open(RECOMMENDED_SONGS_FILE, 'r') as file:
            return set(line.strip() for line in file)
    return set()

def save_recommended_songs(songs):
    """Saves recommended songs to a file."""
    with open(RECOMMENDED_SONGS_FILE, 'a') as file:
        for song in songs:
            file.write(f"{song}\n")

def get_random_tracks(limit=10):
    """
    Fetches random songs from YouTube and lists recommendations.
    
    :param limit: Number of random songs to fetch
    :return: A list of song information
    """
    query = "popular music"
    search_results = fetch_from_youtube_api(query, max_results=50)
    recommended_songs = load_recommended_songs()

    formatted_tracks = [
        f"{item['snippet']['title']} by {item['snippet']['channelTitle']} (https://www.youtube.com/watch?v={item['id']['videoId']})"
        for item in search_results
    ]
    
    new_tracks = [track for track in formatted_tracks if track not in recommended_songs]
    if new_tracks:
        random_tracks = random.sample(new_tracks, min(limit, len(new_tracks)))
        save_recommended_songs(random_tracks)
        return random_tracks
    else:
        return ["No new recommendations available."]

def main():
    """Main function to fetch and display songs."""
    num_tracks = 10  # Set the number of songs to fetch
    random_songs = get_random_tracks(num_tracks)
    
    print("Recommended Songs:")
    if random_songs:
        for i, song in enumerate(random_songs, start=1):
            print(f"{i}. {song}")
    else:
        print("No new song recommendations found.")

if __name__ == "__main__":
    main()
