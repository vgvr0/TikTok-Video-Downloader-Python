# TikTok Video Downloader

## Description:
The TikTok Video Saver is a Python tool that allows users to download TikTok videos using the tiktok_scraper library. It provides a simple command-line interface to download videos from TikTok profiles and includes additional functionalities:

1. Automatic Video Renaming: After downloading a video, it automatically renames the file with a “tiktok_” prefix for easy identification.
2. Video Metadata Retrieval: The tool can also fetch metadata for the downloaded video, including details like the number of likes, comments, and views.

## Installation:
Clone this repository to your local machine:
```git clone https://github.com/your-username/tiktok-video-saver.git```

Install the necessary dependencies:
```pip install tiktok-scraper```

## Usage:
1. Run the `download_tiktok_video.py` script, providing the TikTok video URL and the output directory:
```python download_tiktok_video.py --url https://www.tiktok.com/@username/video/123456789 --output /path/to/directory```
The video will be downloaded and saved in the specified folder. The renamed video will have the “tiktok_” prefix.
2. To retrieve video metadata, use the `get_video_metadata` function within the same script.

## Contribution:
Contributions are welcome! Feel free to add new features or improve existing ones.

## License:
This project is licensed under the MIT License. See the LICENSE file for more details.
