#!/usr/bin/env python
# source https://news.ycombinator.com/item?id=19078825

import traceback
import pdb
import sys


def main():
    # some WIP code that maybe raises an exception
    raise BaseException("oh no, exception!")
    return 0


if __name__ == "__main__":
    try:
        ret = main()
    except:
        traceback.print_exc()
        pdb.post_mortem()
    else:
        sys.exit(ret)
