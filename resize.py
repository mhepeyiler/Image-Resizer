import numpy as np
import requests
import argparse
import os 
import cv2

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("-f","--file",required=True,
        help="image file to resize")
    ap.add_argument("-r","--ratio",required=True,
        help="ratio to resize")
    ap.add_argument("-o","--output",required=True,
        help="new name of file")
    ap.add_argument("-a","--algorithm",default="bicubic",
        help="resize algorithm, that can be 'neighbour, bilinear, bicubic, lanczos' \n default=bicubic")
    args = vars(ap.parse_args())

    if args["algorithm"].lower() == "neighbour":
        a = cv2.INTER_NEAREST
    elif args["algorithm"].lower() == "bilinear":
        a = cv2.INTER_LINEAR
    elif args["algorithm"].lower() == "bicubic":
        a = cv2.INTER_CUBIC
    elif args["algorithm"].lower() == "lanczos": 
        a = cv2.INTER_LANCZOS4
    else: 
        pass

    img = cv2.imread(args["file"])
    width, height = img.shape[:2]
    ratio = float(args["ratio"])
    new_img = cv2.resize(img,(int(height*ratio) ,int(width*ratio)),interpolation=a)
    cv2.imwrite(args["output"],new_img)


if __name__ == "__main__":
    main()