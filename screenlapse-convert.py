import glob
import os
import pathlib
import subprocess
import sys

import cv2


def main():
    files = sorted(
        glob.glob(str(pathlib.Path().absolute()) + "\\data\\img\\*"),
        key=os.path.getmtime,
    )
    # Have a peek at the first image to work out the resolution
    test_img = cv2.imread(files[0])
    height, width, _ = test_img.shape
    size = (width, height)

    print("Processing " + str(len(files)) + " images and creating video...")
    out = cv2.VideoWriter("screenlapse.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 10, size)
    for file in files:
        out.write(cv2.imread(file))
    print("Finishing up...")
    out.release()
    print("Done!")
    if sys.platform == "win32":
        subprocess.run(["explorer.exe", "."], shell=True)


if __name__ == "__main__":
    main()
