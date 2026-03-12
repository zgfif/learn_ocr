def normalize_string(text: str) -> str:
    """
    Replace newline characters with spaces and strip leading/trailing whitespace.
    """
    return text.replace('\n', ' ').strip()
