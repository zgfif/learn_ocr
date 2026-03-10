from app.result import Result
import os
from tests.fixtures.questions import question1, question2, question3




def test_result_save():
    temp_file = './temp.csv'
    questions = [question1, question2, question3]

    assert os.path.exists(temp_file) is False

    Result(questions=questions).save(path=temp_file)

    assert os.path.exists(temp_file) is True

    lines: list[str] = []

    with open(file=temp_file, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            lines.append(line)
    
    assert lines[0] == 'id|question|options\n'
    assert lines[1] == "1|How are you?|Fine - True, Bad - False, Not good - True\n"


    if os.path.exists(temp_file):
        os.remove(temp_file)


