# TokenCounter

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

TokenCounter is a simple, user-friendly Python tool with a graphical user interface (GUI) to count tokens in Python projects or individual files. It uses OpenAI's `tiktoken` library to accurately calculate tokens based on LLM tokenization (e.g., for GPT models). Perfect for developers working with AI models, code analysis, or estimating context lengths for prompts.

This tool allows you to:
- Select single files.
- Scan entire folders recursively.
- Choose multiple files at once.

It's lightweight, requires minimal setup, and is completely free and open-source.

## Features

- **Intuitive GUI**: Built with Tkinter for easy use – no command-line required.
- **Flexible Selection**: Count tokens in one file, multiple files, or whole directories (recursive scan for `.py`, `.txt`, `.md` files; customizable).
- **Accurate Token Counting**: Powered by `tiktoken` for precise BPE tokenization (default: `cl100k_base` encoding, like GPT-4).
- **Detailed Output**: Shows tokens per file and total, with scrollable results.
- **Cross-Platform**: Runs on Windows, macOS, and Linux.

## Installation

1. **Prerequisites**:
   - Python 3.8 or higher (download from [python.org](https://www.python.org/downloads/)).
   - Tkinter (usually included with Python; if not, install via your package manager, e.g., `sudo apt install python3-tk` on Ubuntu).

2. **Install Dependencies**:

pip install tiktoken
text
3. **Download the Tool**:
- Clone this repository:

git clone https://github.com/blobb999/TokenCounter.git
cd TokenCounter
text
- Or download the ZIP and extract it.

## Usage

1. **Run the Tool**:

python token_counter.py
text
- A GUI window will open.

2. **How to Use**:
- **Single File**: Click "Einzelne Datei auswählen" and pick a file.
- **Folder**: Click "Ordner auswählen (rekursiv)" to scan a directory.
- **Multiple Files**: Click "Mehrere Dateien auswählen" for batch selection.
- Results appear in the scrollable text box, including per-file tokens and total.

Example Output:

C:/path/to/file.py: 1234 Tokens
C:/path/to/another.py: 567 Tokens

Gesamt: 1801 Tokens in 2 Dateien
text
3. **Customization**:
   - Edit the code to change the encoding (e.g., `tiktoken.get_encoding("gpt2")`).
   - Extend file extensions in `process_files` (e.g., add `.js` for JavaScript).

## Screenshots

![Main GUI](screenshots/main_gui.png)  
*The main interface with buttons for selection.*

![Results Example](screenshots/results.png)  
*Example output after scanning files.*

(Upload your own screenshots to the `screenshots/` folder.)

## Contributing

Contributions are welcome! Fork the repo, make changes, and submit a pull request. Issues or feature requests? Open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Free for all – use, modify, and share as you like!

## Acknowledgments

- Built with [tiktoken](https://github.com/openai/tiktoken) for token counting.
- Inspired by needs for LLM context management in code projects.

If you find this useful, star the repo or share it! Questions? Open an issue.