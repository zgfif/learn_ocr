from app.question_extracting import QuestionExtracting
from app.option import Option
from app.question import Question


images: list[str] = [
    './tests/fixtures/parts/part_img_0.png',
    './tests/fixtures/parts/part_img_1.png',
    './tests/fixtures/parts/part_img_2.png',
    './tests/fixtures/parts/part_img_3.png',
]


def test_question_extracting():
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

    got = QuestionExtracting(images=images).perform()

    assert isinstance(got, Question)
    assert len(got.options) == len(expected.options)
    assert got == expected



images2: list[str] = [
    './tests/fixtures/parts2/part_img_0.png',
    './tests/fixtures/parts2/part_img_1.png',
    './tests/fixtures/parts2/part_img_2.png',
    './tests/fixtures/parts2/part_img_3.png',
]



def test_question_extracting2():
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

    got = QuestionExtracting(images=images2).perform()

    assert isinstance(got, Question)
    assert len(got.options) == len(expected.options)
    assert got == expected
