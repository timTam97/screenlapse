import glob
import os
import pathlib

import cv2


def main():
    img_list = []
    files = sorted(
        glob.glob(str(pathlib.Path().absolute()) + "\\img\\*"), key=os.path.getmtime
    )
    # Have a peek at the first image to work out the resolution
    test_img = cv2.imread(files[0])
    height, width, _ = test_img.shape
    size = (width, height)

    print("Processing " + str(len(files)) + " images...")
    for file in files:
        img_list.append(cv2.imread(file))
    out = cv2.VideoWriter("screenlapse.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 10, size)
    print("Creating video...")
    for i in range(len(img_list)):
        out.write(img_list[i])
    print("Finishing up...")
    out.release()
    print("Done!")


if __name__ == "__main__":
    main()
