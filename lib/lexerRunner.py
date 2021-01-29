import argparse

from lib.stoneToken import StoneToken
from lib.lexer import LineReader
from lib.lexer import Lexer


if __name__ == "__main__":
    # use --file or -f set filename, default is samples/first.stone
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--file", "-f", type=str)
    args = argparser.parse_args()

    filename = "samples/first.stone"
    if args.file is not None:
        filename = args.file

    print("File: " + filename)
    with open(filename, 'r') as f:
        reader = LineReader(f)
        lexer = Lexer(reader)
        token = lexer.read()
        if token != None: print(token.getText())
        while token != StoneToken.EOF:
            token = lexer.read()
            if token != None: print(token.getText())

