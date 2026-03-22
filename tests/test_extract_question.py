import pytest

from app.question_extracting import QuestionExtracting
from app.option import Option
from app.question import Question
from app.load_image import load_image



@pytest.fixture
def ticked_template():
    image = load_image(path='./img/ticked.png')
    if image is None:
        pytest.skip('can not load ticked template')
    return image



@pytest.fixture
def unticked_template():
    image = load_image(path='./img/unticked.png')
    if image is None:
        pytest.skip('can not load ticked template')
    return image



@pytest.fixture
def images_4731():
    images_paths: list[str] = [
        './tests/fixtures/parts/part_img_0.png',
        './tests/fixtures/parts/part_img_1.png',
        './tests/fixtures/parts/part_img_2.png',
        './tests/fixtures/parts/part_img_3.png',
    ]
    return [load_image(path=image_path) for image_path in images_paths]



@pytest.fixture
def images_4732():
    images_paths: list[str] = [
        './tests/fixtures/parts2/part_img_0.png',
        './tests/fixtures/parts2/part_img_1.png',
        './tests/fixtures/parts2/part_img_2.png',
        './tests/fixtures/parts2/part_img_3.png',
    ]
    return [load_image(path=image_path) for image_path in images_paths]



def test_question_extracting(images_4731, ticked_template, unticked_template):
    expected = Question(
        text='Sie befinden sich in der Probezeit und sind bisher nicht auffällig geworden. Welche Folgen können eintreten, wenn Sie an dem Verkehrszeichen „Halt. Vorfahrt gewähren.“ nicht anhalten und dadurch andere Verkehrsteilnehmer gefährden?',
        options = [
            Option(
                text='Anordnung zum erneuten Ablegen einer theoretischen Fahrerlaubnisprüfung', 
                correctness=False
            ),
            Option(
                text='Anordnung zur Teilnahme an einem Aufbauseminar für Fahranfänger', 
                correctness=True
            ),
            Option(
                text='Eintrag in das Fahreignungsregister', 
                correctness=True
            ),
        ]
    )
    got = QuestionExtracting(
        images=images_4731, 
        ticked_template=ticked_template, 
        unticked_template=unticked_template
    ).extract()
    assert got == expected



def test_question_extracting2(images_4732, ticked_template, unticked_template):
    expected = Question(
        text='Wie lange dauert normalerweise die Probezeit?',
        options = [
            Option(
                text='2 Jahre', 
                correctness=True
            ),
            Option(
                text='1 Jahr', 
                correctness=False
            ),
            Option(
                text='3 Jahre', 
                correctness=False
            ),
        ]
    )
    got = QuestionExtracting(
        images=images_4732, 
        ticked_template=ticked_template, 
        unticked_template=unticked_template
    ).extract()
    assert got == expected



def test_question_extracting_when_no_images(ticked_template, unticked_template):
    got = QuestionExtracting(
        images=[], 
        ticked_template=ticked_template, 
        unticked_template=unticked_template
    ).extract()
    assert got is None


# def test_when_error_with_patterns(mocker):
    
#     images: list[str] = [
#         './tests/fixtures/parts/part_img_0.png',
#         './tests/fixtures/parts/part_img_1.png',
#         './tests/fixtures/parts/part_img_2.png',
#         './tests/fixtures/parts/part_img_3.png',
#     ]
#     question = QuestionExtracting(images=images)
#     mocker.patch.object(question, 'ticked_template', return_value=None)
#     mocker.patch.object(question, 'unticked_template', return_value=None)
#     mocker.patch.object(question, 'images', return_value=images)

#     with pytest.raises(ValueError, match='Could not load patterns'):
#         question.perform()
