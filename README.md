# YTmusic Suggestion

# YouTube Music Recommendation Tool

This Python script uses the YouTube Data API to fetch random music recommendations. It tracks previously recommended songs to avoid duplicates and provides fresh suggestions every time.

## Features
- Fetches popular music recommendations from YouTube.
- Avoids recommending songs already suggested in the past.
- Saves recommended songs to a local file for reference.

---

## Requirements
- Python 3.7 or higher
- `google-api-python-client` library (for interacting with the YouTube Data API)
- A valid YouTube Data API key

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo/youtube-music-recommendation.git
    cd youtube-music-recommendation
    ```

2. Install required Python libraries:
    ```bash
    pip install google-api-python-client
    ```

3. Set up your YouTube API key:
   - Visit [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project (or use an existing one).
   - Enable the **YouTube Data API v3** for your project.
   - Create an API key and replace the `YOUR_YOUTUBE_API_KEY` in the code with your key.

---

## Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. The program will fetch and display a list of recommended songs:
    ```
    Recommended Songs:
    1. Song Title by Channel Name (https://www.youtube.com/watch?v=videoID)
    2. ...
    ```

3. Previously recommended songs are saved to a file (`youtube_recommended_songs.txt`) to prevent duplicates in future runs.

---

## Code Explanation

### Key Functions
1. **`fetch_from_youtube_api(query, max_results=10)`**:
   - Sends a search query to the YouTube Data API.
   - Returns a list of videos matching the query.

2. **`load_recommended_songs()`**:
   - Loads previously recommended songs from a local file.

3. **`save_recommended_songs(songs)`**:
   - Saves newly recommended songs to the same file.

4. **`get_random_tracks(limit=10)`**:
   - Fetches songs using the API and recommends tracks that haven't been suggested before.

5. **`main()`**:
   - Orchestrates the entire process and displays recommendations.

---

## Notes
- Make sure your YouTube API key has sufficient quota for API calls.
- You can modify the `query` parameter in `get_random_tracks()` to customize the type of music recommendations.

---

## License
This project is licensed under the MIT License.
