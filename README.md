# ASCII Player

This is a script for generating an ASCII art video by converting each frame of a video into an ASCII art representation.

> [!IMPORTANT]  
> The following project has reached its end of life and is no longer maintained. No further updates or support will be provided.

## Prerequisites

- Python 3.x
- pip

## Installation

1. Clone this repository: `git clone https://github.com/VEERT00X/ASCIIPlayer.git`
2. Install the required libraries: `pip install -r requirements.txt`

## Usage

The script takes the path of the video file as an argument. If no argument is provided, the script will prompt for the file path.

The generated ASCII art video will be displayed in the terminal.

To run the script, use the following command:

```bash
python _main_.py [path_to_video_file]
```

## Customization

- You can customize the ASCII characters used in the output by modifying the `ASCII` variable in the script.
- You can decide whether or not to show the original video alongside the ASCII art by passing the `-p` or `--preview` flag when running the script.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

Copyright (c) 2023-2025 VEERT00X
