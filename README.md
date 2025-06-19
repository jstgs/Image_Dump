# 📱 Android Image Collector & Hasher

A lightweight Python-based **Android forensics tool** that uses `adb` to collect image files from a connected **rooted Android phone** and computes their **MD5** and **SHA-256** hashes for forensic analysis.

---

## 🔍 Features

- ✅ Automatically detects connected Android device via ADB
- 📥 Pulls image directories (`DCIM/Camera` and `DCIM/Screenshots`) to local storage
- 🔒 Computes **MD5** and **SHA-256** hashes of all collected image files
- 📂 Organizes data per-device in timestamped folders
- 🐍 Easy to extend for more forensic modules

---

## ⚙️ Requirements

- Python 3.7+
- [ADB (Android Debug Bridge)](https://developer.android.com/tools/adb) installed and in your system PATH
- Rooted Android device with `adb` debugging enabled

---
