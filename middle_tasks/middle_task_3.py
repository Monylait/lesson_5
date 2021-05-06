# TODO:
#  Примечание: все цвета указаны в hex формате
#  0. Создать окно приложения размерами 400х300
#       0.1 Цвет фона окна- #BABABA
#  1. Разместить в нем кнопку:
#       1.1 Размеры кнопки - 340x340
#       1.2 Расположить кнопку по центру окна приложения
#       1.3 Цвет фона кнопки - #252525
#       1.4 Текст кнопки - "Show message"
#       1.5 Размер текста кнопки - 36
#       1.5 Цвет текста кнопки - #FFFFFF
#  2. По нажатию на кнопку должно отображаться окно MessageBox с текстом, при каждом нажатии выбранным случайным образом
#       из списка messages
#  https://www.figma.com/file/HaLJnBXkaz1JpSGChjz03R/middle_task_3

messages = [
    "self.setGeometry(650, 400, 500, 150)",
    'self.pushButton.setStyleSheet("background-color: red")',
    'self.pushButton.resize(100, 100)',
    'self.pushButton.clicked.connect(self.func)'
]

