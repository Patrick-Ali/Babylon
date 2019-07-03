import json

class JSON():
    def addData(self, file, data):
        '''Add data to a specific file'''
        end = '.json'
        full = str(file+end)
        with open(full, 'w') as f:
            json.dump(data,f)
    
    def getData(self, file, key, value = None): #, value
        '''Open a file and get the specific data from it'''
        end = '.json'
        full = str(file+end)
        with open(full, 'r') as f:
            data = json.load(f)
            print(data)
            if value == None:
                return data[key]#[value]
            else:
                return data[key][value]
            
    def loadData(self, file):
        '''Open a file and get all the data from it'''
        end = '.json'
        full = str(file+end)
        with open(full, 'r') as f:
            data = json.load(f)
            return data

    def mergeDict(self, dict1, dict2):
        print("Here")
        print(dict1)
        print(dict2)
        for key in dict1:
            print(dict1[key])
            dict2[key] = dict1[key]
        return dict2
        
if __name__ == '__main__':
    test = JSON()
    data = {
        "Test":"Data"
        }
    #dataWhole = test.loadData()
    file = "test"
    dataWhole = test.loadData(file)
    #z = {**data, **dataWhole}
    z = test.mergeDict(dataWhole, data)
    print(z)
    test.addData(file, z)
    print(test.getData(file, "Test"))
    
