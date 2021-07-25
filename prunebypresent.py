from __future__ import print_function
import sys
import glob
import shutil
import os

in2 = list(map(os.path.basename, glob.glob(sys.argv[2]+ "/*")))

for f in glob.glob(sys.argv[1]):
    if os.path.basename(f) in in2:
        print("REMOVING DUP:", f)
        os.remove(f)
