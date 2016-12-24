#!/usr/bin/python3

from pathlib import Path
from subprocess import call

    
def main(directory, file_ext):    
    path = Path(directory)	

    files = list(path.rglob("*.{}".format(file_ext)))

    l = ["vi"]
    l += [str(files[0]), "-c"]
    cmd_str = ""
    for i, fn in enumerate(files[1:-1]):
        cmd_str += "tabe {} | ".format(fn)

    cmd_str += "tabe {}".format(files[-1]) 

    l.append(cmd_str)

    call(l)


if __name__=="__main__":

    import argparse

    parser = argparse.ArgumentParser(description="open files with same extension with vim, one per tab")


    parser.add_argument("extension", type=str, help="name extension of files")

    parser.add_argument("-d", "--directory", type=str, default=".", help="name of package the class belongs to")

    
    args = parser.parse_args()

    main(args.directory, args.extension)

