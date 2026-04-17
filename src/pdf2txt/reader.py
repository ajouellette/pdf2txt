from pypdf import PdfReader


def read_pdf(
    fname: str, page_range: None | tuple[int | None, int | None] = None
) -> str:
    """
    Extract text from a pdf file.

    Args:
        fname (str): Path to the pdf file.
        page_range (None | tuple[int | None, int | None]): Optional page range to extract. Page range is given as a tuple (start, end) and is inclusive.

    Returns:
        str: The extracted text.

    Assumptions:
        - Start and end of page range are greater than zero.
        - End of page range is greater than start.

    Raises:
        RuntimeError: If the page range exceeds the number of pages in the document.
    """
    pages = []
    reader = PdfReader(fname)
    if page_range is not None:
        start = page_range[0] - 1 if page_range[0] is not None else 0
        end = page_range[1] if page_range[1] is not None else len(reader.pages)
        # these conditions should not occur:
        assert start >= 0 and end >= 0
        assert end > start
        if start >= len(reader.pages) or end > len(reader.pages):
            raise RuntimeError(
                f"Asked for an invalid page range {page_range}. Document only has {len(reader.pages)} pages."
            )
        page_slice = slice(start, end)
    else:
        page_slice = slice(0, len(reader.pages))
    for page in reader.pages[page_slice]:
        pages.append(page.extract_text())
    return "\n".join(pages)
