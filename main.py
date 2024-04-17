from os import getcwd, remove, listdir
from os.path import join, isfile, isdir
from pydub import AudioSegment
import sys

def convert(file):
    print(f"Converting {file} to FLAC...")
    file_stripped = strip_extension(file)
    stream = AudioSegment.from_wav(file)
    stream.export(f"{file_stripped}.flac", format="flac")

def is_type(file, extension):
    file_type = file.split(".")[-1]
    return file_type == extension

def strip_extension(file):
    file_parts = file.split(".")[:-1]
    file_without_ext = ".".join(file_parts)
    return file_without_ext

def check_dir(path):
    contents = listdir(path)
    print(contents)
    for content in contents:
        current_path = join(path, content)
        if isfile(current_path):
            if is_type(current_path, "wav"):
                convert(current_path)
                print("Removing .WAV file...")
                remove(current_path)
                print("Proceeding to next file...")
        elif isdir(current_path):
            check_dir(current_path)
        else:
            print(f"ERROR: {current_path} is not a valid path or file.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ROOT = sys.argv[1]
    print(f"Starting from: {ROOT}")
    check_dir(ROOT)
    print("Done!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
