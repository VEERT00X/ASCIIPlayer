import os
import sys
import cv2
from PIL import Image

# Configuration
ASCII = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", "!", "^", "&", "~", "-", "_"]

def get_file_path():
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = input("Enter file path: ")
    print("File path loaded: " + file_path)
    return file_path

FILE_PATH = get_file_path()

# Check for preview flag
SHOW_PREVIEW = "-p" in sys.argv or "--preview" in sys.argv

# Functions
def resized_gray_image(image, new_width):
    width, height = image.size
    aspect_ratio = height / width * 0.55
    new_height = max(1, int(aspect_ratio * new_width))
    resized_image = image.resize((new_width, new_height)).convert('L')
    return resized_image

def pixEl(image):
    pixels = image.getdata()
    characters = "".join([ASCII[pixel // 25] for pixel in pixels])
    return characters

def generate(image, new_width):
    new_image_data = pixEl(resized_gray_image(image, new_width))
    total_pixels = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, total_pixels, new_width)])
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        pass
    sys.stdout.write(ascii_image + "\n")

# Determine terminal size
def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80 

cap = cv2.VideoCapture(FILE_PATH)

# Main
if __name__ == "__main__":
    terminal_width = get_terminal_width()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if SHOW_PREVIEW:
                cv2.imshow("frame", frame)

            generate(Image.fromarray(frame), new_width=terminal_width)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("Exited Successfully!")
