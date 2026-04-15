from pypdf import PdfReader


def read_pdf(fname: str) -> str:
    """Extract text from a pdf file."""
    pages = []
    reader = PdfReader(fname)
    for page in reader.pages:
        pages.append(page.extract_text())
    return "\n".join(pages)
