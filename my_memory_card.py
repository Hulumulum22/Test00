from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QRadioButton, QGroupBox, QVBoxLayout,
                             QHBoxLayout, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([]) #создали приложение


question_list = []

question_list.append(Question('сколько стоит echo sabre', '2550', '4600', '1000', '0'))
question_list.append(Question('предмет который создаёт клонов',  'manta_style', 'tarasq', 'echo sabre', 'black king bar'))
question_list.append(Question('первый скил на цк', 'стан противника', 'притягивает противника', 'создаёт клонов', 'тпхает на спавн'))





window = QWidget() #создали окно
window.setWindowTitle('Memo Card') #заголовок окна

btn_OK = QPushButton('Ответить') #создали кнопку
lb_Question = QLabel('Самый сложный вопрос в мире') #создали виджет под вопрос

'''Сборки формы с вопросом'''
RadioGroupBox = QGroupBox() #Создали групбокс (форма вопроса)
rbtn_1  = QRadioButton('Вариант1') #создали 4 кнопки-переключателя
rbtn_2  = QRadioButton('Вариант2')
rbtn_3  = QRadioButton('Вариант3')
rbtn_4  = QRadioButton('Вариант4')

RadioGroup = QButtonGroup() #создали группу
RadioGroup.addButton(rbtn_1)#добавили кнопки в группу
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout() #создали Г линию
layout_ans2 = QVBoxLayout() #создали В линию
layout_ans3 = QVBoxLayout() #создали В линию

layout_ans2.addWidget(rbtn_1) #добавили на одну В линию 2 кнопки
layout_ans2.addWidget(rbtn_2)

layout_ans3.addWidget(rbtn_3) #добавили на другую В линию 2 кнопки
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2) # на Г линию прикрепили В
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) #поместили макет в групбокс

'''Сборка формы с результатом'''
AnsGroupBox = QGroupBox()
lb_Result = QLabel('Прав или не прав')
lb_Correct = QLabel('Ответ тут')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct, alignment = Qt.AlignCenter)

AnsGroupBox.setLayout(layout_res)


'''Начинаем сборку макета окна'''
layout_line1 = QHBoxLayout() #создали 3 Г линии
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = Qt.AlignCenter) #прикрепили виджеты на линии
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addWidget(btn_OK)

layout_card = QVBoxLayout() #главная вертикальная линия
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

window.setLayout(layout_card)
AnsGroupBox.hide() #спрятали форму с вопросом

def show_result():
    RadioGroupBox.hide() #спрятали форму с вопросом
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)    

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q:Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)

    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()
    

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        window.score +=1

    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно')

def next_question():
    window.total += 1
    print("----")
    print('Всего вопросов:', window.total - 1)
    print('Всего ответов:', window.score)
    print("----")
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)



def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.cur_question = -1
window.resize(400,300)

btn_OK.clicked.connect(click_OK)

window.total = 0
window.score = 0
next_question()
window.show() #показали окно
app.exec_() #программа будет закрывать только при нажатии на крестик

