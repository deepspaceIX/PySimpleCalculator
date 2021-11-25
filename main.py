from tkinter import *
import tkinter

# Varibles-----------------------------------------------

# Colors-------------------------------------------------
mediumGray = '#131314'
lighterMediumGray = '#2b2b2d'
white = '#ffffff'

# Numbers------------------------------------------------
answer1 = 0
answer2 = 0
currentSymbol = ""

# Bools--------------------------------------------------
isCalculating = False
start = False

# MainGui------------------------------------------------
window = Tk()
window.title('PySimpleCalculator')
window.geometry('250x400')
window.minsize(250, 400)
window['background'] = mediumGray

# AnswerLabel--------------------------------------------
answerLabel = Label(window, text=answer1, font=("Arial", 25), fg=white, background=lighterMediumGray)
answerLabel.place(relwidth=1, relheight=0.2)

# Functions----------------------------------------------
def isInt(num):
    if type(num) == int:
        return True

def isFloat(num):
    if type(num) == float:
        return True

def calcluate(isNumber, number):
    global isCalculating
    global answer1
    global answer2
    global currentSymbol
    if start == True:
        if isCalculating == False:
            if isNumber == True:
                stringAnswer = str(answer1)
                stringNumber = str(number)
                if answer1 == 0:
                    answer1 = stringNumber
                else:
                    answer1="%s%s"%(stringAnswer,stringNumber)
                
                if isInt(answer1):
                    answer1 = int("%s%s"%(stringAnswer,stringNumber))
                answerLabel.config(text = answer1)
            else:
                if number == 'divide':
                    isCalculating = True
                    currentSymbol = 'divide'
                    answerLabel.config(text = answer2)
                if number == 'multiply':
                    isCalculating = True
                    currentSymbol = 'multiply'
                    answerLabel.config(text = answer2)
                if number == 'add':
                    isCalculating = True
                    currentSymbol = 'add'
                    answerLabel.config(text = answer2)
                if number == 'subtract':
                    isCalculating = True
                    currentSymbol = 'subtract'
                    answerLabel.config(text = answer2)
        else:
            if isNumber == True:
                stringAnswer = str(answer2)
                stringNumber = str(number)
                if answer2 == 0:
                    answer2 = stringNumber
                else:
                    answer2="%s%s"%(stringAnswer,stringNumber)
                    
                if isInt(answer2):
                    answer2 = int("%s%s"%(stringAnswer,stringNumber))
                answerLabel.config(text = answer2)
            else:
                if number == 'enter':
                    answer1 = int(answer1)
                    answer2 = int(answer2)
                    if currentSymbol == "add":
                        answer1 += answer2
                    if currentSymbol == "subtract":
                        answer1 -= answer2
                    if currentSymbol == "multiply":
                        answer1 *= answer2
                    if currentSymbol == "divide":
                        answer1 /= answer2
                    answerLabel.config(text = answer1)
                    isCalculating = False
                    answer2 = 0
                    currentSymbol = ""

def resetAll():
    if start == True:
        global answer1
        global answer2
        global isCalculating
        global currentSymbol
        answer1 = 0
        answer2 = 0
        isCalculating = False
        currentSymbol = ""
        answerLabel.config(text = answer1)

# CalculatorButtons--------------------------------------
button1 = Button(window, text=' 1 ', font=("Arial", 12), fg=white, background=lighterMediumGray, command= lambda: calcluate(True, 1))
button1.place(relwidth=.25, relheight=0.2, relx=0, rely=.2)

button2 = Button(window, text=' 2 ', font=("Arial", 12), fg=white, background=lighterMediumGray, command= lambda: calcluate(True, 2))
button2.place(relwidth=.25, relheight=0.2, relx=.25, rely=.2)

button3 = Button(window, text=' 3 ', font=("Arial", 12), fg=white, background=lighterMediumGray, command= lambda: calcluate(True, 3))
button3.place(relwidth=.25, relheight=0.2, relx=.5, rely=.2)

buttonDivide = Button(window, text=' / ', font=("Arial", 12), fg=white, background=lighterMediumGray, command = lambda: calcluate(False, 'divide'))
buttonDivide.place(relwidth=.25, relheight=0.2, relx=.75, rely=.2)

button4 = Button(window, text=' 4 ', font=("Arial", 12), fg=white, background=lighterMediumGray, command= lambda: calcluate(True, 4))
button4.place(relwidth=.25, relheight=0.2, relx=0, rely=.4)

button5 = Button(window, text=' 5 ', font=("Arial", 12), fg=white, background=lighterMediumGray, command= lambda: calcluate(True, 5))
button5.place(relwidth=.25, relheight=0.2, relx=0.25, rely=.4)

button6 = Button(window, text=' 6 ', font=("Arial", 12), fg=white, background=lighterMediumGray, command= lambda: calcluate(True, 6))
button6.place(relwidth=.25, relheight=0.2, relx=0.5, rely=.4)

buttonMultiply = Button(window, text=' x ', font=("Arial", 12), fg=white, background=lighterMediumGray, command = lambda: calcluate(False, 'multiply'))
buttonMultiply.place(relwidth=.25, relheight=0.2, relx=0.75, rely=.4)

button7 = Button(window, text=' 7 ', font=("Arial", 12), fg=white, background=lighterMediumGray, command= lambda: calcluate(True, 7))
button7.place(relwidth=.25, relheight=0.2, relx=0, rely=.6)

button8 = Button(window, text=' 8 ', font=("Arial", 12), fg=white, background=lighterMediumGray, command= lambda: calcluate(True, 8))
button8.place(relwidth=.25, relheight=0.2, relx=0.25, rely=.6)

button9 = Button(window, text=' 9 ', font=("Arial", 12), fg=white, background=lighterMediumGray, command= lambda: calcluate(True, 9))
button9.place(relwidth=.25, relheight=0.2, relx=0.5, rely=.6)

buttonSubtract = Button(window, text=' - ', font=("Arial", 12), fg=white, background=lighterMediumGray, command = lambda: calcluate(False, 'subtract'))
buttonSubtract.place(relwidth=.25, relheight=0.2, relx=0.75, rely=.6)

buttonClear = Button(window, text=' CE ', font=("Arial", 12), fg=white, background=lighterMediumGray, command=lambda: resetAll())
buttonClear.place(relwidth=.25, relheight=0.2, relx=0, rely=.8)

button0 = Button(window, text=' 0 ', font=("Arial", 12), fg=white, background=lighterMediumGray, command= lambda: calcluate(True, 0))
button0.place(relwidth=.25, relheight=0.2, relx=0.25, rely=.8)

buttonEnter = Button(window, text=' = ', font=("Arial", 12), fg=white, background=lighterMediumGray, command = lambda: calcluate(False, 'enter'))
buttonEnter.place(relwidth=.25, relheight=0.2, relx=0.5, rely=.8)

buttonAdd = Button(window, text=' + ', font=("Arial", 12), fg=white, background=lighterMediumGray, command = lambda: calcluate(False, 'add'))
buttonAdd.place(relwidth=.25, relheight=0.2, relx=0.75, rely=.8)

start = True

window.mainloop()
