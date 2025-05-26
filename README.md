# WhatsApp Spam Automation

A Python script with a modern dark-themed GUI that automates sending messages on WhatsApp Web using PyAutoGUI. This script sends a series of animal-themed messages to a specified contact, with easy Start/Stop controls.

## ⚠️ Disclaimer

This tool is for educational purposes only. Please use responsibly and respect others' privacy. Spamming can be considered harassment and may violate WhatsApp's terms of service.

## 🚀 Features

- Modern dark-themed graphical interface
- Start and Stop buttons for easy control
- Automated message sending through WhatsApp Web
- Customizable recipient name
- Pre-defined list of animal names
- Responsive and user-friendly design

## 📋 Prerequisites

- Python 3.11
- UV package manager
- PyAutoGUI library
- WhatsApp Web access
- Active internet connection

## 🛠️ Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/WhatsApp-Spam-Automation-Python.git
cd WhatsApp-Spam-Automation-Python
```

2. Install UV if you haven't already:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Install the required dependencies:

```bash
uv add pyautogui
```

## 💻 Usage

1. Run the script:

```bash
uv run main.py
```

2. Enter the name of the contact in the GUI
3. Switch to the WhatsApp Web chat window
4. Click **Start Spamming** to begin sending messages
5. Click **Stop** at any time to immediately stop the automation

> **Note:** The GUI window will stay on top for easy access to the Stop button. The status label will indicate when the script is running or stopped.

## 🔧 How it Works

The script:

1. Prompts for the recipient's name in the GUI
2. Waits for you to switch to WhatsApp Web
3. Sends messages in the format: "_[Name]_ `aik [animal] hai`"
4. Includes a 1-second delay between messages (with responsive stop)
5. Allows you to stop the automation at any time with the Stop button

## 📝 Message Format

Messages are sent in the following format:

```
_[Name]_ `aik [animal] hai`
```

For example:

```
_John_ `aik lion hai`
```

## ⚡ Dependencies

- `pyautogui`: For automating keyboard and mouse actions
- `tkinter`: For the graphical user interface
- `time`, `threading`: For timing and background processing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Important Notes

- Keep WhatsApp Web window active while the script is running
- Do not move your mouse or use your keyboard while the script is running
- Use responsibly and respect others' privacy
