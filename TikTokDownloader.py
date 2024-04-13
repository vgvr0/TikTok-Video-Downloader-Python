from tiktok_scraper import TikTokScraper
import os

def download_tiktok_video(video_url, output_dir):
    """
    Downloads a TikTok video from the given URL and saves it to the specified directory.

    Args:
        video_url (str): URL of the TikTok video.
        output_dir (str): Destination directory where the downloaded video will be saved.
    """
    try:
        scraper = TikTokScraper()
        video_path = scraper.download_video(video_url, output_dir)
        print("Downloaded video:", video_path)

        # Additional functionality: Rename the downloaded video
        video_name = os.path.basename(video_path)
        new_video_name = f"tiktok_{video_name}"
        new_video_path = os.path.join(output_dir, new_video_name)
        os.rename(video_path, new_video_path)
        print("Renamed video:", new_video_path)

        # Additional functionality: Get video metadata
        video_metadata = scraper.get_video_metadata(video_url)
        print("Video metadata:", video_metadata)

    except Exception as e:
        print("Error:", str(e))

# Example usage
if __name__ == "__main__":
    tiktok_url = "https://www.tiktok.com/@username/video/123456789"
    download_directory = "/path/to/directory"
    download_tiktok_video(tiktok_url, download_directory)
