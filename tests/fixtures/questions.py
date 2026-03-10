from app.question import Question
from app.option import Option



question1 = Question(
    text='How are you?',
    options=[
        Option(text='Fine', correctness=True), 
        Option(text='Bad', correctness=False), 
        Option(text='Not good', correctness=True)
    ]
)

question2 = Question(
    text='Where do you live?',
    options=[
        Option(text='Odessa', correctness=True), 
        Option(text='Kiev', correctness=False), 
        Option(text='Kherson', correctness=False),
    ]
)

question3 = Question(
    text='Your speaking language(s)?',
    options=[
        Option(text='English', correctness=True),
        Option(text='Deutch', correctness=False),
        Option(text='Russsian', correctness=True),
    ]
)
