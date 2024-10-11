# Keylogger using `pynput`

This is a simple keylogger script written in Python using the `pynput` library. It logs all keypresses (including spaces) into a text file called `keyfile.txt`.

## Features

- Logs all key presses into a text file.
- Supports both regular keys (e.g., letters, numbers) and special keys (e.g., space).

## Installation

You need to install the `pynput` library, which allows the program to listen to keyboard inputs. You can install it using the following commands, depending on your operating system:
#### On Unix/Linux (macOS, Ubuntu, etc.)
Open the terminal and run:

```bash
pip install pynput
```

## On Windows (CMD)
Open the Command Prompt and run:

```bash
pip install pynput
```
## How to Run

1. Clone or download this repository to your local machine.
2. Place the Python script in your desired directory.
3. Open a terminal in the script's directory and run the program:

    ```bash
    python keylogger_friendly.py
    ```
or,

   ```bash   
    py keylogger_friendly.py
   ```

4. The program will start logging keystrokes in the background. It will create or append to a file called `keyfile.txt` in the same directory as the script.

---

## How it Works

- **Keyboard Listener**: The script listens for all keypress events on your keyboard.
- **Logging to File**: Every keypress is logged to a file called `keyfile.txt`.
- **Space Handling**: The script explicitly handles space keypresses to avoid errors.

---

## Code Explanation

The script does the following:

1. Imports `pynput` to listen to keyboard inputs.
2. Defines the `keyPressed` function that writes the keypresses to `keyfile.txt`.
3. Handles regular and special keys (like spaces) using the `hasattr()` function.
4. Starts the keyboard listener and keeps the script running with `input()`.

### Example of key logging:

If you type "Hello World", the content of `keyfile.txt` will be:

```plaintext
Hello World
```
## Important Notes

This script is intended for educational purposes only. Always ensure that you have permission before logging keystrokes on any system.  
You can stop the program by closing the terminal or pressing `Ctrl + C`.
