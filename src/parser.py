import pdfplumber


def extract_text(file_path):

    # Try reading as PDF
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

            if text.strip():
                return text.strip()
    except:
        pass

    # Try reading as normal text file
    try:
        with open(file_path, "rb") as f:
            content = f.read()

        try:
            return content.decode("utf-8").strip()
        except:
            return content.decode("latin-1").strip()
    except:
        pass

    raise ValueError("Unsupported file format")
