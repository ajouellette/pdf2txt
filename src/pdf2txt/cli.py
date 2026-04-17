import argparse
import re

from .reader import read_pdf


def parse_page_range(page_range: str) -> tuple[int, int]:
    """Parse a page range, ensuring that it is valid."""
    pattern = r"^(\d+)-(\d+)$"
    match = re.match(pattern, page_range)
    if match is not None:
        pages = (int(match.group(1)), int(match.group(2)))
    else:
        raise ValueError("Invalid page range format. Must be given as START-END.")

    if pages[0] < 1:
        raise ValueError(
            "Invalid page range. START must be greater than or equal to 1."
        )
    if pages[0] > pages[1]:
        raise ValueError(
            "Invalid page range. END must be greater than or equal to START."
        )

    return pages


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("PDF")
    parser.add_argument(
        "-p",
        "--pages",
        default=None,
        type=str,
        help="Page range (inclusive) to extract. Must be given as START-END.",
    )
    args = parser.parse_args()

    pages = parse_page_range(args.pages) if args.pages else None

    # extract and print to stdout
    full_text = read_pdf(args.PDF, page_range=pages)
    print(full_text)
