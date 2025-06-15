# 🚀 Quick-Loader

A lightweight and user-friendly CLI wrapper for [yt-dlp](https://github.com/yt-dlp/yt-dlp) that lets you download videos and audio from YouTube with simple, readable commands.

---

## 📦 Features

- 🎞 Download videos and audio using easy commands
- 🧭 Search and download by link or title _(coming soon)_
- 🔧 Format, and output path flags
- 💡 Minimalistic CLI interface with helpful flags
- ✅ Works out of the box with Python

---

## ⚙️ Installation

Make sure you have `Python 3.7+` and `ffmpeg` installed.

### 1. Clone the repo

```bash
git clone https://github.com/Qu0i/Quick-Loader.git
cd Quick-Loader
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Make the script globally available (Linux/macOS)

```bash
chmod +x ql
sudo ln -s $(pwd)/ql /usr/local/bin/ql
```

Now you can run `ql` from anywhere in your terminal 🎉

---

## 🧪 Usage

```bash
ql "https://youtu.be/dQw4w9WgXcQ?si=kWTZwI5JS3TUi3Rx" -f mp3 -r 720p -o ~/Downloads
```

### Available Flags:

| Flag                 | Description                          | Example       |
| -------------------- | ------------------------------------ | ------------- |
| `-f`, `--format`     | Download format (`mp3`, `mp4`, etc.) | `-f mp4`      | |
| `-o`, `--output`     | Output file path                     | `-o ~/Videos` |
| `--version`    | Show current version                 | `--version`   |
| `-v`, `--video`     | Download video only `(without audio)` | `-v`      | |

---

## 🔍 Roadmap

- [x] Basic download support
- [x] Playlist download support
- [ ] Support for downloading specific parts of videos _(planned)_
- [ ] 

---

## 📄 License

MIT License © 2025 [Qu0i](https://github.com/Qu0i)
