import yt_dlp

def download_instagram_reel(instagram_url):
    # Define yt-dlp options
    ydl_opts = {
          'format': 'mp4',  # Select best audio format
          'outtmpl': '%(title)s.%(ext)s',  # Save file with video title as name
    }

    # Download the audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([instagram_url])

if __name__ == "__main__":
    url = input("Enter Instagram Reel URL: ")
    download_instagram_reel(url)
    print("Download complete! ✅ The MP4 file is saved in the same folder.")
    
    
