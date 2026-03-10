# from app.option_text import ImageText



# image1_option1: str = '2 Jahre\n'

# image2_option1: str = """Anordnung zur Teilnahme an einem
# Aufbauseminar für Fahranfänger
# """

# image1_full: str = """Wie lange dauert normalerweise die Probezeit?

# n 2 Jahre
# Ü 1 Jahr
# Ü 3 Jahre
# """

# image2_full: str = """Sie befinden sich in der Probezeit und sind bisher
# nicht auffällig geworden. Welche Folgen können
# eintreten, wenn Sie an dem Verkehrszeichen „Halt.
# Vorfahrt gewähren.“ nicht anhalten und dadurch
# andere Verkehrsteilnehmer gefährden?

# Anordnung zum erneuten Ablegen einer
# theoretischen Fahrerlaubnisprüfung

# Anordnung zur Teilnahme an einem
# Aufbauseminar für Fahranfänger

# n Eintrag in das Fahreignungsregister
# """


# def test_image1_option_text():
#     image_path: str = './IMG_4731.png'
#     start_coord: tuple = (37 + 170, 404)
#     end_coord: tuple = (37 + 1200, 404 + 150)
#     got = ImageText(
#         image_path=image_path, 
#         start_coord=start_coord, 
#         end_coord=end_coord
#     ).fetch()
#     assert image1_option1 == got



# def test_image2_option_text():
#     image_path: str = './IMG_4732.png'
#     start_coord: tuple = (37 + 150, 894)
#     end_coord: tuple = (37 + 1200, 894 + 150)
#     got = ImageText(
#         image_path=image_path, 
#         start_coord=start_coord, 
#         end_coord=end_coord
#     ).fetch()
#     assert image2_option1 == got



# def test_image1_full_text():
#     image_path: str = './IMG_4731.png'
#     got = ImageText(image_path=image_path, start_coord=(0, 215), end_coord=(1286, 2235)).fetch()
#     assert image1_full == got



# def test_image2_full_text():
#     image_path: str = './IMG_4732.png'
#     got = ImageText(image_path=image_path, start_coord=(0, 215), end_coord=(1286, 2235)).fetch()
#     assert image2_full == got
