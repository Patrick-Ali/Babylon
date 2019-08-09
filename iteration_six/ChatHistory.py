import csv
from pathlib import Path

class ChatHistory():
    """
        Class handels writing and reading to the
        user's chat history file.
    """
    
    def readFile(self, path):
        """
            Method takes in the path to a CSV file.
            It then opens the file in read mode and
            returns the content of the file in an array (list). 
        """
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
        """
            Method takes in the path to a CSV file and
            the information to be added to the file.
            The file is open in append mode and the message
            is appended to the file.
        """
        file = Path(path)
        with open(file, 'a') as chat:
            chatWriter =  csv.writer(chat, delimiter=',', quotechar='"')
            chatWriter.writerow(['"' + msg + '"'])

    def checkFile(self, path):
        """
            Takes in the path to a file and checks whthere it exists.
            If the file does not exist the file will be created.
            Otherwise the method will return True when the file exists
            or has been created.
        """
        file = Path(path)
        if not file.is_file():
            temp = open(file, 'w')
            print("Creating " + temp.name)
            temp.close()
            
        return True
            
    

if __name__ == "__main__":
    pass
