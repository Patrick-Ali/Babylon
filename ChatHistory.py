import csv
from pathlib import Path

class ChatHistory():

    
    def __init__(self):
        pass

    def readFile(self, path):
        file = Path(path)
        chatHistory = []
        with open(file, 'r') as chat:
            chatReader = csv.reader(chat, delimiter=',', quotechar='"')
            for row in chatReader:
                if row != []:
                    temp = row[0]
                    temp = temp.replace('"', '')
                    chatHistory.append(temp)
        return chatHistory

    def writeFile(self, path, msg):
        file = Path(path)
        with open(file, 'a') as chat:
            chatWriter =  csv.writer(chat, delimiter=',', quotechar='"')
            chatWriter.writerow(['"' + msg + '"'])

    def checkFile(self, path):
        file = Path(path)
        if not file.is_file():
            temp = open(file, 'w')
            print("Creating " + temp.name)
            temp.close()
            
        return True
            
    

if __name__ == "__main__":
    
    #checkFile("./user.csv")
    hold = ChatHistory()
    if(hold.checkFile("./user.csv")):
        hold.writeFile("./user.csv", "Hello")
        chat = hold.readFile("./user.csv")
        for msg in chat:
            print(msg)
