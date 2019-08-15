from JSON import JSON
from RulesExtra import Rules

class Expands():
    reader = JSON()
    rules = Rules()
    
    def domain(self):
        dom = input("What domain would you like to add? \n Domain Name: ")
        hold = self.reader.loadData("domains")
        domains = hold["domains"]
        domains.append(dom.lower())
        new_doms = {"domains":domains}
        self.reader.addData("domains", new_doms)
    
    def operation(self):
        dom_name = input("What is the domain name? \n Domain Name: ")
        op_name = input("What is the operation name? \n Name: ")
        op = input("What is the operation assembly instruction? Instructions: ")
        dom_check = self.rules.checkFile((dom_name + ".json"), False)
        if dom_check == 0:
            data = {op_name.lower():op.lower()}
            self.reader.addData(dom_name.lower(), data)
        else:
            hold = self.reader.loadData(dom_name)
            hold[op_name.lower()] = op.lower()
            self.reader.addData(dom_name, hold)
            
    def program_function(self):
        hold = self.reader.loadData("py")
        funcs = hold["functions"]
        func_name = input("Function Name: ")
        data = {}
        d = True
        while d == True:
            key_value = input("Enter data in key value pairs seperated by a comma (e.g. key,value), to end type end. \n Data: ")
            if key_value == "end":
                d = False
            else:
                key_value = key_value.replace(":", ",")
                #key_value = key_value.replace(" ", "")
                temp = key_value.split(",")
            if len(temp) == 2:
                data[temp[0].lower()] = temp[1].lower()
            else:
                print("Not recognised")
        funcs[func_name] = data
        hold["functions"] = funcs
        self.reader.addData("py", hold)

if __name__ == "__main__":
    
    test = Expand()
    test.domain()
    test.operation()
    test.program_function()

        
        
