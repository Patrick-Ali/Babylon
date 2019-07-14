import json

class JSON():
    """
        Class handels JSON files and data. Capable of reading, writing, and
        getting specific pieces of data from the JSON file.
    """
    def addData(self, file, data):
        '''Add data to a specific file'''
        end = '.json'
        full = str(file+end)
        with open(full, 'w') as f:
            json.dump(data,f)
    
    def getData(self, file, key, value = None):
        '''Open a file and get the specific data from it'''
        end = '.json'
        full = str(file+end)
        with open(full, 'r') as f:
            data = json.load(f)
            
            if value == None:
                return data[key]
            else:
                return data[key][value]
            
    def loadData(self, file):
        '''Open a file and get all the data from it'''
        end = '.json'
        full = str(file+end)
        with open(full, 'r') as f:
            data = json.load(f)
            return data

    def mergeDict(self, dict_one, dict_two):
        '''Merge two dictionaires into one'''
        for key in dict_one:
            dict_two[key] = dict_one[key]
        return dict_one
        
if __name__ == '__main__':
    pass
    
