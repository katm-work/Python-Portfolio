import yt_dlp

def download_youtube_playlist(url):
    # Set the hardcoded download path and filename template
    save_path = '/Users/kmend/Videos/ytdl/%(playlist)s/%(title)s.%(ext)s'  # Update this to your desired path
    
    # Set the download options
    ydl_opts = {
        'outtmpl': save_path,  # Set the output path
        'format': 'best',      # Download the best quality video and audio
        'noplaylist': False,    # Ensure that playlists are not ignored
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Playlist has been downloaded successfully and saved to '{save_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    playlist_url = input("Enter the URL of the YouTube playlist: ")
    
    download_youtube_playlist(playlist_url)
