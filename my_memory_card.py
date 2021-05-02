'''
#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout, QRadioButton, QMessageBox, QGroupBox
app = QApplication([])
main_win = QWidget()
main_win.resize(400,300)
main_win.setWindowTitle('Memory card')

question = QLabel('Какой национальности не существует?')
btn_answer = QPushButton('Ответить')

RadioGroupBox = QGroupBox("Варианты ответов")
rb1 = QRadioButton('Энцы')
rb2 = QRadioButton('Чулымцы')
rb3 = QRadioButton('Смурфы')
rb4 = QRadioButton('Алеуты')

lay1 = QHBoxLayout()
lay2 = QVBoxLayout()
lay3 = QVBoxLayout()

lay2.addWidget(rb1)
lay2.addWidget(rb2)
lay3.addWidget(rb3)
lay3.addWidget(rb4)
lay1.addLayout(lay2)
lay1.addLayout(lay3)

RadioGroupBox.setLayout(lay1)

layt1 = QHBoxLayout()
layt2 = QHBoxLayout()
layt3 = QHBoxLayout()
layt4 = QVBoxLayout()

layt1.addWidget(question, alignment = Qt.AlignHCenter| Qt.AlignVCenter)
layt2.addWidget(RadioGroupBox

layt3.addWidget(btn_answer, alignment = Qt.AlignHCenter)

layt4.addLayout(layt1)
layt4.addLayout(layt2)
layt4.addLayout(layt3, stretch = 5)
layt4.setSpacing(5)







main_win.setLayout(layt4)

main_win.show()
app.exec_()
'''














#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QButtonGroup, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_l = []
questions_l.append(Question('Сколько лет императору всея Руси(В.В.Путину)?', '68', '21', '72', '2020'))
questions_l.append(Question('В каком году родился император всея Руси(В.В.Путин)?', '1952', '1948', '0', '137лет до н.э', ))
questions_l.append(Question('Какого числа родился император всея Руси(В.В.Путин)?', '7 октября', '8 марта', '1 августа', '29 февраля'))

app=QApplication([])
main_win=QWidget()
main_win.resize(400,300)
main_win.setWindowTitle("Memory Card")

l_question=QLabel("В каком году родился Пушкин?")

btn_ok=QPushButton("Ok")
RadioButtonBox=QGroupBox("Варианты ответов")
rbtn_1= QRadioButton("1799")
rbtn_2= QRadioButton("1399")
rbtn_3= QRadioButton("1999")
rbtn_4= QRadioButton("2005")

RadioGroup= QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioButtonBox.setLayout(layout_ans1)

# результаты
AnsGroupBox= QGroupBox("Результаты теста")
ib_Result= QLabel("Прав ты или нет?")
ib_Correct = QLabel("Ответ будет тут!")

layout_res = QVBoxLayout()
layout_res.addWidget(ib_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(ib_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()

layout_line1.addWidget(l_question, alignment= (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioButtonBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_results():
    RadioButtonBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Следующий вопрос")

def show_question():
    RadioButtonBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    l_question.setText(q.question)
    ib_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    ib_Result.setText(res)
    show_results()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика')
        print('Всего вопросов: ', main_win.total)
        print('Правильных ответов: ', main_win.score)
        print('Рейтинг:', (main_win.score/main_win.total*100), '%')
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')
        print('Рейтинг:', (main_win.score/main_win.total*100), '%')

def next_question():
    main_win.total += 1
    print('Статистика')
    print('Всего вопросов: ', main_win.total)
    print('Правильных ответов: ', main_win.score)
    our_question = randint(0, len(questions_l) - 1)
    q = questions_l[our_question]
    ask(q)


def click_OK():
    if "Ответить" == btn_ok.text():
        check_answer()
    else:
        next_question()

main_win.setLayout(layout_card)
btn_ok.clicked.connect(click_OK)

main_win.score = 0
main_win.total = 0

next_question()
main_win.show()
app.exec_()
