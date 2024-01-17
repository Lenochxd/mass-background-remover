# Mass Background Remover

This Python program allows you to use the ClipDrop API or the [rembg](https://github.com/danielgatis/rembg) library to remove the background from multiple images at once. Simply place the images you want to process in the `input` folder, run the program, and the processed images will be saved to the `output` folder.

## Usage

1. Clone this repository or [download](https://github.com/LeLenoch/mass-background-remover/releases/latest) the source code.
2. Choose the background removal method:
   - For ClipDrop API: Obtain an API key from the [ClipDrop website](https://clipdrop.co/apis/account) and place it in "YOUR_API_KEY.txt".
   - For rembg: No additional setup is required.
3. Place the images you want to process in the "input" folder.
4. Run the program with `python main.py`.
5. The processed images will be saved to the "output" folder.

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [requests library](https://pypi.org/project/requests/) (`pip install requests`)
- [rembg library](https://pypi.org/project/rembg/) (`pip install rembg`)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
