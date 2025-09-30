# YouTube Video Downloader

Download **full YouTube videos or playlists** in the **best available quality**, with **metadata and high-resolution thumbnails embedded**. Runs entirely locally, so no restrictions or ads.

---

## Features

* Download a single video or entire playlist.
* Automatically merges best video + best audio.
* Embeds metadata (title, description, author) into the video file.
* Embeds high-resolution thumbnail.
* Skips already downloaded videos.
* Shows progress for playlists (`[current / total]`).

---

## Usage

### Mac OS Users

```bash
# Install yt-dlp if not installed
python3 -m pip install --user yt-dlp

# Add yt-dlp to PATH if needed
nano ~/.zshrc
# Add line at end:
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
source ~/.zshrc

# Run the downloader
python3 ytvideo_downloader.py <video-or-playlist-url>
```

### Windows Users

```powershell
# Install yt-dlp
python -m pip install --user yt-dlp

# Run the downloader
python ytvideo_downloader.py <video-or-playlist-url>
```

### Linux Users

```bash
# Install yt-dlp
python3 -m pip install --user yt-dlp

# Run the downloader
python3 ytvideo_downloader.py <video-or-playlist-url>
```

---

## Examples

* Download a single video:

```bash
python3 ytvideo_downloader.py "https://youtu.be/_ijaEtNzZgw"
```

* Download a full playlist:

```bash
python3 ytvideo_downloader.py "https://www.youtube.com/playlist?list=PLQNp-BCxMEnIeSoWfDbZXzJURVnItRyBz"
```

---

## Folder Structure

* Downloads are saved under `DownloadedVideos/<Playlist Name>` for playlists.
* Single videos go under `DownloadedVideos/NA`.

---

## Troubleshooting

1. **yt-dlp not found**: Make sure `yt-dlp` is installed and added to your system PATH.
2. **Python version warning**: macOS default Python may be old; update to Python 3.10+ for best support.
3. **Thumbnail file remains**: The script now automatically deletes the `.jpg` after embedding.

---

If you have any issue or comments, please leave a comment, I will try to resolve it as soon as possible.

---

**Author:** Sumit Kumar

**GitHub Repository:** [https://github.com/Madotra/Youtube-video-downloader](https://github.com/Madotra/Youtube-video-downloader)
