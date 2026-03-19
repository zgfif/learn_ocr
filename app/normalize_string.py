def normalize_string(text: str) -> str:
    """
    Replace newline characters with spaces and strip leading/trailing whitespace.
    
    Parameter
    ---------
    text : str
        Input text for processing.

    Returns
    -------
    str
        Normalized text.
    """
    return " ".join(text.split())
