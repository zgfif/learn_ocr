from app.ocr_core import ocr_core


EXPECTED ="""1:48 AM & atll & @) 55,

Punkte: 2

Sie befinden sich in der Probezeit und sind bisher
nicht auffallig geworden. Welche Folgen konnen
eintreten, wenn Sie an dem Verkehrszeichen ,Halt.
Vorfahrt gewahren.” nicht anhalten und dadurch
andere Verkehrsteilnehmer gefahrden?

Anordnung zum erneuten Ablegen einer
theoretischen Fahrerlaubnispriifung

Anordnung zur Teilnahme an einem
Aufbauseminar fiir Fahranfanger

n Eintrag in das Fahreignungsregister

B e
> [w ]

[IKIED

"""

EXPECTED2 = """1:48 AM & atll & @) 55,

Punkte: 2 b4

Wie lange dauert normalerweise die Probezeit?

n 2 Jahre
D 1 Jahr
D 3 Jahre

B e
> [w ]

[IKIED

"""

def test_ocr_core():
    got = ocr_core('IMG_4732.png')
    assert got == EXPECTED


def test_second_ocr_core():
    got = ocr_core('IMG_4731.png')
    assert got == EXPECTED2