import pytest

from app.extract_text import extract_text
from app.load_image import load_image



def test_extract_text():
    input_data = load_image(path="./tests/fixtures/parts/part_img_0.png")
    
    if input_data is None:
        pytest.skip("input data is None") 
    
    expected: str = (
        'Sie befinden sich in der Probezeit und sind bisher nicht auffällig geworden. ' 
        'Welche Folgen können eintreten, wenn Sie an dem Verkehrszeichen „Halt. '  
        'Vorfahrt gewähren.“ nicht anhalten und dadurch andere Verkehrsteilnehmer gefährden?'
    )

    got: str = extract_text(image=input_data)
    assert got == expected



def test_extract_text_when_path_is_none():
    input_data = None

    with pytest.raises(ValueError) as excinfo:
        extract_text(input_data)  # type: ignore[arg-type]
    assert 'Image must not be None' in str(excinfo.value)



def test_extract_text_when_bad_image_file():
    input_data = 'sadlkfjald;fkasdlfkjasdf'

    with pytest.raises(RuntimeError) as excinfo:
        extract_text(input_data)  # type: ignore[arg-type]
    assert 'OCR failed' in str(excinfo.value)
