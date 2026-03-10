def normalize_string(string: str) -> str:
    """
    Replace \\n with white space and remove heading and trailing white spaces.
    """
    txt = string.replace('\n', ' ')
    return txt.strip()
