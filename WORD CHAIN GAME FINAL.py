userword = open( "addword.txt", "r", encoding='utf-8') #if the file size is too big you should put utf-8
import random 

computer = []

while True:
    word = userword.readline()
    computer.append(word)
    if not word:
        break

while True:
    word = userword.readline()
    find = word.find(" ")
    if find == -1:
        computer.append(word)
    else:
        word = word.replace("i", "")
        computer.append(word)
    if not word:
        break

userword.close()

#2
while True:
    userword = input("  ")
    answerList = []
    wordlen = len(userword)
    lastword = userword[wordlen-1]

    for nword in computer:
        exist = nword.find(lastword)
        if exist == 0:
            answerList.append(nword)
        else:
            pass

    if len(answerList) == 0:
        print('?')
        add = input("add:")
        if len(add) > 1:
            addword = open( "addword.txt", "r", encoding='utf-8')
            addword.write('%s`n'%add)
            addword.close()
            computer.append(add)
        else:
            pass
    else:
        answer = random.choice(answerList)
        print("Computer word:", answer)


#3 no overlapping output words from computer answers
        
while True:
    if isAnswerUsed(answer, answerList):
        answer = open( "addword.txt", "r", encoding='utf-8')
        continue
    else:
        break

def isAnswerUsed(answer,answerList):
    if answer in answerList:
        return true
    else:
        return flase

        
