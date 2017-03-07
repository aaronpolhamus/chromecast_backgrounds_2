"""Written for python 3.x. Useful little script for bulk downloading images to
local drives from links. To run:
(0) Make sure you are running python3.
(1) cd to chromecast-backgrounds repo
(2) From terminal, run: `$ python move_to_dir.py --out_dir /your/desired/path'
"""

import os
import argparse
import urllib.request
from shutil import copyfile

parser = argparse.ArgumentParser(description="Download the links in README.md to local file")
parser.add_argument('--out_dir', action='store', default='/tmp/chromecast_images', dest='out_dir')
args = parser.parse_args()

if not os.path.exists(args.out_dir):
    os.makedirs(args.out_dir)

with open('README.md') as links_file:
    links = links_file.read().splitlines()

links = [x[4:-1] for x in links]
N = len(links)

count = 0
for link in links:
    count += 1
    if count % 10 == 0:
        print('Downloaded {0} out of {1} images'.format(count, N))

    try:
        data = urllib.request.urlretrieve(link)
        copyfile(data[0], '{0}/bg_{1}.jpg'.format(args.out_dir, count))
    except Exception as err:
        print(err)
