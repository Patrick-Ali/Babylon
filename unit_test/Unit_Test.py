import sys
sys.path.append('../')
from ChatHistory import ChatHistory as ch

def test_check():
    #assert ch.checkFile("./user.csv") == True
    hold = ch()
    assert hold.checkFile("./user.csv") == True
    #return hold.checkFile("./user.csv")

def test_wirte():
    hold = ch()
    chat = len(hold.readFile("./user.csv"))
    hold.writeFile("./user.csv", "Hello")
    chat2 = len(hold.readFile("./user.csv"))

    assert chat2 == (chat+1)


#if __name__ == "__main__":
    #print(test_check())
