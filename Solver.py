from Interpreter import parse
import logging
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error('wrong number of args')
        exit()
    else:
        print(parse(sys.argv[1]))