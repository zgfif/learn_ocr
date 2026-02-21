from app.question import Question
import csv



class Result:
    COLUMNS: tuple = ('id', 'question','options')

    def __init__(self, questions: list[Question]) -> None:
        self.questions = questions


    def save(self, path: str) -> None:
        """Save to csv file."""
        with open(path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')
            self._write_content(writer=writer)            


    def _write_content(self, writer) -> None:
        """Write content to csv file."""
        writer.writerow(self.COLUMNS)
        id = 1
        for question in self.questions:
            writer.writerow([id, question.text, question.options])
            id += 1
