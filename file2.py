def game():
    return 50

yourScore = game()
yourScore = yourScore

with open("hiscore.txt") as f:
    hiscore = f.read()
    hiscore = int(hiscore) 

if(yourScore>hiscore):
    yourScore = str(yourScore)
    hiscore = str(hiscore)

    file = open("hiscore.txt","w")
    file.write(hiscore)
    file.close()
else:
    yourScore = str(yourScore)
    file = open("hiscore.txt","w")
    file.write(yourScore)
    file.close()
 
