#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Lane detection script
'''

import argparse
import matplotlib.image as mpimg
from engine import process_image, process_video


def main(args):

    outfile = args.dest
    # Append input extension to default destination fine
    if len(outfile.split('/')[-1].split('.')) == 1:
        extension = args.source.split('.')[-1]
        outfile = f"{args.dest}.{extension}"

    # Allow video processing using the args.video flag
    if args.video:
        process_video(args.source, outfile, thickness=args.thickness, write_gif=args.gif)
    else:
        res = process_image(args.source, thickness=args.thickness)
        mpimg.imsave(outfile, res)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Lane detector',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("source", type=str, help="File to process")
    parser.add_argument("--dest", type=str, default='lane-detection-result', help="Output file name")
    parser.add_argument("--video", dest="video", help="should the source be processed as a video",
                        action="store_true")
    parser.add_argument("--gif", dest="gif", help="should the output be written as a GIF",
                        action="store_true")
    parser.add_argument("--thickness", type=int, default=5, help="Thickness of drawn lines")

    args = parser.parse_args()
    main(args)
