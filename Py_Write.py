from JSON import JSON

import subprocess

#Create function
#Create variables
#Create ability to perform operation
#Create return statement

class PyCreate():

    reader = JSON()
    
    def create_function(self, name, param_name, operation):
        indent = "   "
        new_line = "\n"
        line = self.reader.getData("py", "function", "code")
        line = line.replace("<name>", name)
        params = []
        for p_name in param_name:
            param = self.create_param(True, p_name)
            params.append(param)
        param = ''
        for p in params:
            param += (p + ", ")
        line = line.replace("<param>", param)
        line_two = self.create_body(operation, params)
        line_three = self.create_return(operation)
        text = line + new_line + indent + line_two + new_line + indent + line_three

        self.write_line("test.py", text)
        
    def create_param(self, func_param, name, value = "[]"):
        param = name
        if not func_param:
            param = name + " = " + value
        return param
            
    def create_body(self, operation, variables):
        # Suggestion - variables, values, operations, return
        line = self.reader.getData("py", operation, "code")
        for var in variables:
           line.replace("<name" + str(var) + ">", var)
        return line
    
    def create_return(self, operation):
        line = self.reader.getData("py", operation, "return")
        return line

    def create_app_run(self, call, params):
        indent = "   "
        new_line = "\n"
        line = self.reader.getData("py", "run")
        line_two = call
        for p in params:
            line_two += (p + ",")
        text = new_line + line + new_line + indent + line_two + ")"
        self.write_line("test.py", text)
            
    def write_line(self, file, text):
        with open(file, 'a') as f:
            f.write(text)
        #f.write('print("Hello World")')
            
    def call_py(self, file):
        #**kwargs, args for input variables
        test = subprocess.run("python " + file,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              check=True,
                              text=True,
                              shell=True)
        #print(test.stdout)
        return test.stdout

if __name__ == '__main__':
    test = PyCreate()
    test.create_function("add", ["num1", "num2"], "add")
    test.create_app_run("add(", ["1", "2"])
    #indent = "   "
    #new_line = "\n"
    #test_call()
    #reader = JSON()
    #line = reader.getData("py", "run")
    #test("test2.py", line + new_line)
    #line1 = reader.getData("py", "print", "beginning")
    #line2 = '"Hello World"'
    #line3 = reader.getData("py", "print", "end")
    #sentence = indent + line1 + line2 + line3 + new_line
    #test("test2.py", sentence)
    #test("test2.py")
