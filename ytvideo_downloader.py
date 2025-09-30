import os
import re
import sys
import subprocess

def sanitize_name(name: str) -> str:
    """Make safe folder/filename."""
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def download_video(video_url: str, base_dir="DownloadedVideos", playlist_name="NA", idx=None, total=None):
    """Download a single video with metadata and high-res thumbnail."""
    print(f"\n=== Downloading from: {video_url} ===")

    folder = os.path.join(base_dir, sanitize_name(playlist_name))
    os.makedirs(folder, exist_ok=True)

    # Use yt-dlp to fetch info first
    info_cmd = ["yt-dlp", "-F", video_url]
    result = subprocess.run(info_cmd, text=True, capture_output=True)
    info_output = result.stdout.strip()
    print("📊 Available formats:\n", info_output if info_output else "⚠️ Could not fetch format details.")

    # Download video + audio merged in best quality
    video_title_cmd = ["yt-dlp", "--get-title", video_url]
    video_title = subprocess.run(video_title_cmd, text=True, capture_output=True).stdout.strip()
    safe_title = sanitize_name(video_title)
    file_path = os.path.join(folder, f"{safe_title}.mp4")

    if os.path.exists(file_path):
        print(f"[{idx}/{total}] Already exists, skipping: {safe_title}" if idx and total else f"Already exists: {safe_title}")
        return "skipped"

    print(f"[{idx}/{total}] Downloading: {safe_title}" if idx and total else f"Downloading: {safe_title}")

    command_download = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        "--merge-output-format", "mp4",
        "--add-metadata",
        "--embed-metadata",
        "--embed-thumbnail",
        "-o", file_path,
        video_url
    ]
    subprocess.run(command_download)

    # Cleanup leftover thumbnail file
    thumb_file = os.path.join(folder, f"{safe_title}.jpg")
    if os.path.exists(thumb_file):
        os.remove(thumb_file)

    return "downloaded"

def download_playlist(playlist_url: str, base_dir="DownloadedVideos"):
    """Download all videos from a YouTube playlist."""
    print(f"\n=== Downloading playlist: {playlist_url} ===")

    # Fetch playlist info using yt-dlp
    result = subprocess.run(
        ["yt-dlp", "--flat-playlist", "--dump-single-json", playlist_url],
        text=True, capture_output=True
    )
    import json
    try:
        playlist_info = json.loads(result.stdout)
        playlist_title = sanitize_name(playlist_info.get("title", "Unknown Playlist"))
        entries = playlist_info.get("entries", [])
    except Exception:
        print("❌ Failed to fetch playlist info. Exiting.")
        return

    total_videos = len(entries)
    downloaded_count = 0
    skipped_count = 0

    for idx, entry in enumerate(entries, start=1):
        video_url = f"https://www.youtube.com/watch?v={entry['id']}"
        result_status = download_video(video_url, base_dir, playlist_title, idx, total_videos)
        if result_status == "downloaded":
            downloaded_count += 1
        else:
            skipped_count += 1

    print("\n✅ Playlist download completed!")
    print(f"Playlist: {playlist_title}")
    print(f"Total videos: {total_videos}")
    print(f"Downloaded: {downloaded_count}")
    print(f"Skipped (already existed): {skipped_count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ytvideo_downloader.py <video-or-playlist-url>")
        sys.exit(1)

    link = sys.argv[1]

    if "playlist?list=" in link:
        download_playlist(link)
    else:
        download_video(link)

if __name__ == "__main__":
    main()
