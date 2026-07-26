# 📁 File Organizer Simple

A lightweight and beginner-friendly Python application that automatically organizes files into categorized folders based on their file extensions. This project helps keep directories clean and demonstrates the use of Python file handling and automation.

---

## 📌 Overview

Managing a folder filled with different file types can be time-consuming. **File Organizer Simple** automates this process by scanning a selected directory and moving files into organized folders such as Images, Documents, Videos, Music, Archives, and more.

This project was created as part of my Python learning journey and showcases practical file automation using Python.

---

## ✨ Features

* 📂 Automatically organizes files by extension
* 🖼️ Separates images, videos, documents, audio, archives, and more
* ⚡ Fast and easy to use
* 🐍 Built entirely with Python
* 💻 Beginner-friendly code structure
* 🔄 Reusable for any folder

---

## 📁 Supported Categories

| Category     | Examples                        |
| ------------ | ------------------------------- |
| 🖼️ Images   | jpg, jpeg, png, gif, bmp, webp  |
| 📄 Documents | pdf, docx, doc, txt, pptx, xlsx |
| 🎥 Videos    | mp4, mkv, avi, mov              |
| 🎵 Audio     | mp3, wav, flac                  |
| 🗜️ Archives | zip, rar, 7z                    |
| 💻 Code      | py, html, css, js, java         |
| 📦 Others    | Unknown file types              |

---

## 📷 Example

### Before

```text
Downloads/
├── photo.jpg
├── report.pdf
├── music.mp3
├── video.mp4
├── project.py
└── archive.zip
```

### After

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Audio/
│   └── music.mp3
├── Videos/
│   └── video.mp4
├── Code/
│   └── project.py
└── Archives/
    └── archive.zip
```

---

## 🛠️ Built With

* Python 3
* os
* shutil
* pathlib (optional)

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/najathkwt35-cloud/file_organizer_simple.git
```

Move into the project folder

```bash
cd file_organizer_simple
```

Run the application

```bash
python organizer.py
```

> Replace `organizer.py` with your actual Python filename if it is different.

---

## 📂 Project Structure

```text
file_organizer_simple/
│
├── organizer.py
├── README.md
└── assets/
```

---

## 🎯 Learning Objectives

This project helped me learn:

* Python programming
* File handling
* Directory management
* Loops and conditions
* Functions
* Error handling
* Automation basics

---

## 🔮 Future Improvements

* GUI version using CustomTkinter
* Drag & Drop folder selection
* Progress bar
* Undo last operation
* Duplicate file detection
* Empty folder cleanup
* Log file generation
* Dark mode interface
* File statistics dashboard
* AI-based image sorting

---

## 🤝 Contributions

Contributions, suggestions, and feature requests are welcome.

Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

### **Al Rinas**

🎓 Software Engineering Student

☁️ Aspiring Cloud Engineer

* GitHub: https://github.com/najathkwt35-cloud
* LinkedIn: https://www.linkedin.com/in/rinas-al-b94b793b4/

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
