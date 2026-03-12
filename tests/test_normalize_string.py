from app.normalize_string import normalize_string



def test_normalize_string():
    string = 'Sie befinden sich in der Probezeit und sind bisher\nnicht auffällig geworden. Welche Folgen können\neintreten, wenn Sie an dem Verkehrszeichen „Halt.\nVorfahrt gewähren.“ nicht anhalten und dadurch\nandere Verkehrsteilnehmer gefährden?\n'

    expected = 'Sie befinden sich in der Probezeit und sind bisher nicht auffällig geworden. Welche Folgen können eintreten, wenn Sie an dem Verkehrszeichen „Halt. Vorfahrt gewähren.“ nicht anhalten und dadurch andere Verkehrsteilnehmer gefährden?'
    
    got = normalize_string(text=string)
    
    assert expected == got



def test_normalize_string2():
    string = 'Anordnung zum erneuten Ablegen einer\ntheoretischen Fahrerlaubnisprüfung\n'

    expected = 'Anordnung zum erneuten Ablegen einer theoretischen Fahrerlaubnisprüfung'
    
    got = normalize_string(text=string)
    
    assert expected == got

