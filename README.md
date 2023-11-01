# Activity Logger

This project is a simple activity logger that captures keyboard inputs and mouse clicks, logging them to a file and taking a screenshot of the screen each time a key is pressed. This can be useful for tracking user activity, debugging, or creating a record of interactions for future reference.

## Features

- **Keyboard Logging**: Logs all keyboard inputs along with the timestamp.
- **Mouse Click Logging**: Takes a screenshot each time a mouse button is pressed.
- **Screenshots**: Takes a screenshot of the entire screen each time a key is pressed.

## Installation

To get started, you need to have Python installed on your system. If you don’t have Python installed, you can download it from [python.org](https://www.python.org/).

Once Python is installed, you need to install the required libraries. Run the following command to install them:

```
pip install pynput pyautogui
```

## Usage

To run the activity logger, simply execute the script:

```
python activity_logger.py
```

This will start the activity logger, and it will begin listening for keyboard and mouse events. Logs will be saved to `activity_logs/key_log.txt`, and screenshots will be saved in the `activity_logs` directory.

## Configuration

You can change the directory where logs and screenshots are saved by modifying the `LOG_DIR` variable at the top of the script.

```python
LOG_DIR = "your_directory"
```

## Limitations

- This script currently only logs key presses and mouse clicks. It does not log key releases or other types of mouse events.
- Screenshots are taken for every key press, which can quickly fill up your disk space if not monitored.

## Contributing

If you have any improvements or bug fixes, please feel free to fork this repository, make your changes, and submit a pull request. Your contributions are welcome!

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

This tool is meant to be used responsibly and ethically. Do not use it to log keystrokes or capture information without proper authorization.
