# 📱 TikTok Video Downloader

> 🚀 Download TikTok videos quickly and easily! A simple yet powerful Python tool.

## ✨ Key Features

🎯 What you can do with this tool:
- 📥 Download TikTok videos using URLs
- 🏷️ Automatic video renaming with 'tiktok_' prefix
- 📊 Video metadata retrieval
- 🛡️ Robust error handling

## 🔧 Prerequisites

- 🐍 Python 3.6 or higher
- 📦 `tiktok-scraper` package

## ⚡️ Installation

### 1️⃣ Clone this repository:
```bash
git clone [repository-url]
cd tiktok-downloader
```

### 2️⃣ Install the required package:
```bash
pip install tiktok-scraper
```

## 📖 Usage

### 🎯 Basic Usage

```python
from tiktok_downloader import download_tiktok_video

# Example
tiktok_url = "https://www.tiktok.com/@username/video/123456789"
download_directory = "/path/to/directory"
download_tiktok_video(tiktok_url, download_directory)
```

### 🔍 Function Parameters

- 🔗 `video_url` (str): The URL of the TikTok video to download
- 📁 `output_dir` (str): The directory where the video will be saved

## 🎉 Output

The script will:
1. ⬇️ Download the video to your specified directory
2. ✏️ Rename the video with a 'tiktok_' prefix
3. 📋 Print the video metadata
4. 💬 Display success/error messages during the process

## 📝 Example Output

```
Downloaded video: /path/to/directory/video123.mp4
Renamed video: /path/to/directory/tiktok_video123.mp4
Video metadata: {video_information_object}
```

## ⚠️ Error Handling

The script includes error handling that will:
- 🚫 Catch and display any errors during download
- 📢 Print informative error messages
- 🛡️ Prevent script crashes due to download failures

## 🤝 Contributing

Feel free to submit issues and enhancement requests! We love community contributions! ✨


## ⚖️ Disclaimer

This tool is for educational purposes only. Please ensure you have the right to download and use any content from TikTok before using this script.

---
### 🌟 Made with ❤️ for the TikTok Developer Community
