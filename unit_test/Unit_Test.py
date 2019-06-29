import sys
sys.path.append('../')
from ChatHistory import ChatHistory as ch

def test_check():
    hold = ch()
    assert hold.checkFile("./user.csv") == True
    

def test_wirte():
    hold = ch()
    chat = len(hold.readFile("./user.csv"))
    hold.writeFile("./user.csv", "Hello")
    chat2 = len(hold.readFile("./user.csv"))

    assert chat2 == (chat+1)
