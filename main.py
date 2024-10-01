#Flash Card design
import random as r
from cmu_graphics import * # type: ignore

#Our code is inspired by 4.7 flashcards and uses some statements from it, codes and functions were used from CMU CS coding document.

#Title

Label('AP Computer Science Flashcards', 200, 50, size=25)

#background

app.background= 'lightblue'

#button that is going to be used for onmousepress to bring up a text box
buttonText = Label('Click', 200, 265, size=50)
button = Rect(buttonText.left-5, buttonText.top-15, 90, 70, fill=None, border=None)

#labels
wordLabel= Label('',200,200,font='Arial',size=10)
definitionLabel= Label('',180,120,font='Arial',size=10)
answerLabel= Label('', 200, 150, font='Arial', size=10)
#a list called words that will be for the flash card

#Lists used 
words = [ 'Sequencing', 'Iteration', 'List', 'Procedure', 'Parameter', 'Selection']

definition = [ 'Application of each step of an algorithm in order of the code given', 'A repetitive portion of an algorithm', 'it repeats until a given condition is met after a specific amount of times', 'An ordered sequence of elements', 'A named group of programming instructions that may have parameters and return values', 'Input variable of a procedure', 'Determines which parts of an algorithm are executed based on a condition being true/false' ]


currentWord=[]
app.currentIndex=0


#groups for future loop
checks = Group(
    
     Line(70, 287, 105, 245, lineWidth= 3),
     Line(50, 267, 70, 287, lineWidth= 3),  
     Line(300, 267, 320, 287, lineWidth= 3),
     Line(320, 287, 355, 245, lineWidth= 3)
    ) 
checks.visible=False

knots = Group(
    Line(50, 280, 90, 240),
    Line(50, 240, 90, 280),
    Line(300, 240, 340, 280),
    Line(340, 240, 300, 280)
    )
knots.visible=False

wordLabel = Label('', 200, 200, font='Arial', size=10)


app.currentIndex = r.randint(0,5)

app.currentWord= definition[app.currentIndex]

wordLabel.value = app.currentWord  


#Function that  utilizes loops and has parameters in it
def checkAnswer(response):
    if words[app.currentIndex]==response:
        wordLabel.value='Correct!'
        app.background = 'lawngreen'
        for check in checks.children:
            checks.visible = True
    else:
        wordLabel.value='Incorrect! '+words[app.currentIndex]
        app.background = 'crimson' 
        for knot in knots.children:
            knots.visible=True
  
#click on the Label that says click to bring up a text box to type the answer in  
def onMousePress(mouseX, mouseY):
    answer=app.getTextInput('What is the word for '+ app.currentWord)
    answerLabel.value=(answer)
    checkAnswer(answer)





 

