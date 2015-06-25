


import random
from graphics import*

class button:
    def __init__(self,point1,point2,text,textcolor,win):
        self.point1 = point1
        self.point2 = point2
        self.text = text
        self.textcolor = textcolor
        self.win = win
        self.tag = self.text
        self.box = Rectangle(point1,point2)
        self.label = Text(Point(((self.point2.getX()+self.point1.getX())/2),((self.point2.getY()+self.point1.getY())/2)),self.tag)
        self.label.setFill(textcolor)
    def display(self):
        self.box.draw(self.win)
        self.label.draw(self.win)
    def contain(self,point):
        self.pointcheck = point
        if (((self.pointcheck.getX()<self.point2.getX()) and (self.pointcheck.getX()>self.point1.getX())) or ((self.pointcheck.getX()<self.point1.getX()) and (self.pointcheck.getX()>self.point2.getX()))) and (((self.pointcheck.getY()<self.point2.getY()) and (self.pointcheck.getY()>self.point1.getY())) or ((self.pointcheck.getY()<self.point1.getY()) and (self.pointcheck.getY()>self.point2.getY()))):
            return True
        else:
            return False
    def undraw(self):
        self.box.undraw()
        self.label.undraw()
    def mark(self):
        self.box.setFill('red')
    def unmark(self):
        self.box.setFill('white')

def main():
    win = GraphWin("Hangman by Zach Porter",800,600)
    win.setCoords(0,0,49,100)
    win.setBackground('white')
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    buttons = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    intro=Text(Point(25,50),"""WELCOME TO H_NGM_N
    Press quit at any point to stop playing
    Instructions:
    1.Try and guess the blank word
    2.Fill in the blanks by selecting letters
    3.For each incorrect guess you lose a chance
    4.You only have 6 chances and once you run out you lose
    5.Win by completely filling in all blanks before
    running out of chances
    Click anywhere to start""")
    intro.setTextColor('blue')
    intro.setFace('courier')
    intro.setStyle('bold')
    hangmantitle = Image(Point(25,50),'hangmantitle.GIF')
    hangmantitle.draw(win)
    win.getMouse()
    hangmantitle.undraw()
    intro.setSize(16)
    intro.draw(win)
    win.getMouse()
    intro.undraw()
    animalbutton = button(Point(3,60),Point(21,35),'animals','purple',win)
    superbutton = button(Point(3,30),Point(21,5),'superheros','purple',win)
    countrybutton = button(Point(28,60),Point(46,35),'countries','purple',win)
    subjectbutton = button(Point(28,30),Point(46,5),'subjects','purple',win)
    
        
    x=0
    y=50
    z=0
    counts = 0
    for letters in alphabet:
        if x >= 49:
            x = 0
        if z%7 == 0:
            y-=10
        buttons[counts]=button(Point(x,y),Point(x+7,y-10),letters,'red',win)
        x+=7
        z+=1
        counts+=1
    quitbutton = button(Point(35,10),Point(49,0),'QUIT','black',win)
    quitnum = 0
    games = 0
    wins = 0
    while quitnum!=1:
        animalbutton.display()
        superbutton.display()
        countrybutton.display()
        subjectbutton.display()
        selectprompt = Text(Point(25,80),"Select a category")
        selectprompt.setFill('blue')
        selectprompt.setSize(20)
        selectprompt.draw(win)
        category = 0
        while category == 0:
            c = win.getMouse()
            if animalbutton.contain(c):
                inputfile = open('animals.txt','r')
                category = 1
            elif superbutton.contain(c):
                inputfile = open('superheros.txt','r')
                category = 1
            elif countrybutton.contain(c):
                inputfile = open('countries.txt','r')
                category = 1
            elif subjectbutton.contain(c):
                inputfile = open('subjects.txt','r')
                category = 1
        selectprompt.undraw()
        animalbutton.undraw()
        superbutton.undraw()
        countrybutton.undraw()
        subjectbutton.undraw()
        wordstring = inputfile.read()
        wordlist = wordstring.split()                
        quitbutton.display()
        quitbutton.unmark()
        for b in buttons:
            b.display()
            b.unmark()
        maxindex = len(wordlist)
        index = random.randrange(0,maxindex)
        selectedword= wordlist[index].upper()
        chances = 6
        individualgame = 0
        showme=""
        hangmanletters=[]
        guesses=[]
        for letters in selectedword:
            if letters == '_':
                hangmanletters.append(' ')
                guesses.append(' ')
            else:
                hangmanletters.append(letters)
                guesses.append('_')
        for letters in hangmanletters:
            showme+=letters
            showme+=" "
        while individualgame != 1:
            guessme=""
            for g in guesses:
                guessme+=g
                guessme+=" "
            if chances == 6:
                deadman = Image(Point(40,75),'chance0.GIF')
                deadman.draw(win)
            elif chances == 5:
                deadman = Image(Point(40,75),'chance1.GIF')
                deadman.draw(win)
            elif chances == 4:
                deadman = Image(Point(40,75),'chance2.GIF')
                deadman.draw(win)
            elif chances == 3:
                deadman = Image(Point(40,75),'chance3.GIF')
                deadman.draw(win)
            elif chances == 2:
                deadman = Image(Point(40,75),'chance4.GIF')
                deadman.draw(win)
            elif chances ==1 :
                deadman = Image(Point(40,75),'chance5.GIF')
                deadman.draw(win)
            tbox = Text(Point(25,70),guessme)
            tbox.setSize(26)
            tbox.draw(win)
            chancestring = "Chances left:"+str(chances)
            sbox =Text(Point(10,80),chancestring)
            sbox.setSize(20)
            sbox.draw(win)
            guess = win.getMouse()
            if quitbutton.contain(guess):
                for b in buttons:
                    b.undraw()
                quitbutton.undraw()
                tbox.undraw()
                sbox.undraw()
                deadman.undraw()
                individualgame = 1
                quitnum = 1
                thanks = Text(Point(25,70),"THANKS FOR PLAYING")
                thanks.setFill('green')
                thanks.setSize(30)
                thanks.draw(win)
                tracker = Text(Point(25,40),"Played "+str(games)+" games and won "+str(wins))
                tracker.setFill('purple')
                tracker.setSize(20)
                tracker.draw(win)
                win.getMouse()
                win.close()
            else:
                blank = ' '
                r = 0
                for b in buttons:
                    if b.contain(guess):
                        blank=alphabet[r]
                        b.mark()
                    r+=1
                if blank != ' ':
                    if blank in hangmanletters:
                        j=0
                        for letters in hangmanletters:
                            if letters==blank:
                                guesses[j]=blank
                            j+=1
                    else:
                        chances-=1
            if chances==0:
                individualgame = 1
                games+=1
                for b in buttons:
                    b.undraw()
                quitbutton.undraw()
                gameover=Text(Point(25,90),"GAME OVER YOU LOSE")
                gameover.setFill('green')
                gameover.setSize(30)
                gameover.draw(win)
                tbox.undraw()
                sbox.undraw()
                deadman.undraw()
                deadman = Image(Point(40,65),'death6.GIF')
                deadman.draw(win)
                tbox = Text(Point(25,70),showme)
                tbox.setSize(26)
                tbox.draw(win)
                replay = Text(Point(25,50),"Play again?")
                replay.setFill('blue')
                replay.setSize(20)
                replay.draw(win)
                yes = button(Point(15,35),Point(24,5),"YES",'green',win)
                no = button(Point(25,35),Point(34,5),"NO",'red',win)
                yes.display()
                no.display()
                breaker = 0
                while breaker == 0:
                    select = win.getMouse()
                    if yes.contain(select):
                        breaker = 1
                        gameover.undraw()
                        yes.undraw()
                        no.undraw()
                        replay.undraw()
                    if no.contain(select):
                        breaker = 1
                        quitnum = 1
                        yes.undraw()
                        no.undraw()
                        replay.undraw()
                        gameover.undraw()
                        tbox.undraw()
                        deadman.undraw()
                        thanks = Text(Point(25,70),"THANKS FOR PLAYING")
                        thanks.setFill('green')
                        thanks.setSize(30)
                        thanks.draw(win)
                        tracker = Text(Point(25,40),"Played "+str(games)+" games and won "+str(wins))
                        tracker.setFill('purple')
                        tracker.setSize(20)
                        tracker.draw(win)
                        win.getMouse()
                        win.close()
            if guesses==hangmanletters:
                individualgame = 1
                wins+=1
                games+=1
                for b in buttons:
                    b.undraw()
                quitbutton.undraw()
                congrats = Text(Point(25,90),"CONGRATULATIONS YOU WIN")
                congrats.setFill('green')
                congrats.setSize(30)
                congrats.draw(win)
                tbox.undraw()
                sbox.undraw()
                tbox = Text(Point(25,70),showme)
                tbox.setSize(26)
                tbox.draw(win)
                replay = Text(Point(25,50),"Play again?")
                replay.setFill('blue')
                replay.setSize(20)
                replay.draw(win)
                yes = button(Point(15,35),Point(24,5),"YES",'green',win)
                no = button(Point(25,35),Point(34,5),"NO",'red',win)
                yes.display()
                no.display()
                breaker = 0
                while breaker == 0:
                    select = win.getMouse()
                    if yes.contain(select):
                        breaker = 1
                        congrats.undraw()
                        yes.undraw()
                        no.undraw()
                        replay.undraw()
                    if no.contain(select):
                        breaker = 1
                        quitnum = 1
                        yes.undraw()
                        no.undraw()
                        replay.undraw()
                        congrats.undraw()
                        tbox.undraw()
                        deadman.undraw()
                        thanks = Text(Point(25,70),"THANKS FOR PLAYING")
                        thanks.setFill('green')
                        thanks.setSize(30)
                        thanks.draw(win)
                        tracker = Text(Point(25,40),"Played "+str(games)+" games and won "+str(wins))
                        tracker.setFill('purple')
                        tracker.setSize(20)
                        tracker.draw(win)
                        win.getMouse()
                        win.close()
            tbox.undraw()
            sbox.undraw()
            deadman.undraw()
main()
                      
