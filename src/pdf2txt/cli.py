import argparse

from .reader import read_pdf

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("PDF")
    args = parser.parse_args()
    full_text = read_pdf(args.PDF)
    print(full_text)

