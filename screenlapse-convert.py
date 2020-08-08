import glob
import os
import pathlib

import cv2


def main():
    img_array = []
    files = sorted(
        glob.glob(str(pathlib.Path().absolute()) + "\\img\\*"), key=os.path.getmtime
    )
    print("Processing " + str(len(files)) + " images...")
    for file in files:
        img = cv2.imread(file)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)
    out = cv2.VideoWriter("screenlapse.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 10, size)
    print("Queueing images for encoding...")
    for i in range(len(img_array)):
        out.write(img_array[i])
    print("Processing video...")
    out.release()
    print("Done!")


if __name__ == "__main__":
    main()
