from yt_dlp import YoutubeDL  # pip install yt-dlp

def download_youtube_video(url, output_path='./downloads'):
    """
    Download a YouTube video (best quality MP4).
    
    Args:
    url (str): YouTube video URL (e.g., 'https://www.youtube.com/watch?v=VIDEO_ID').
    output_path (str): Directory to save the video (default: './downloads').
    
    Returns:
    dict: Info about the downloaded video if successful, None otherwise.
    """
    try:
        # Configure options for video download
        ydl_opts = {
            'format': 'best[ext=mp4]/best',  # Prefer MP4, fallback to best
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output filename template
            'noplaylist': True,  # Download single video, not playlist
        }
        
        # Download the video
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Video downloaded successfully to {output_path}!")
        return ydl.extract_info(url, download=False)  # Return metadata
        
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

# Example usage
if __name__ == "__main__":
    VIDEO_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your URL
    download_youtube_video(VIDEO_URL)