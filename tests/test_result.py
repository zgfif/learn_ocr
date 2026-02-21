from app.result import Result
import os
from tests.fixtures.questions import question1, question2, question3



def test_result_save():
    temp_file = './temp.csv'
    questions = [question1, question2, question3]

    assert os.path.exists(temp_file) is False

    Result(questions=questions).save(path=temp_file)

    assert os.path.exists(temp_file) is True

    if os.path.exists(temp_file):
        os.remove(temp_file)


