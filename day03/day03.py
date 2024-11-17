print('hello5')
# width = 10
# height = 20
# area = width * height
# print(area)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--width', help='Width in pixels', required = True, type=int)
parser.add_argument('--height', help='Height in pixels in pixels', required = True, type=int)

args = parser.parse_args() 
width = args.width
height = args.height

area = width * height
print(area)