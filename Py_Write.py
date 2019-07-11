from JSON import JSON

import subprocess

#Create function
#Create variables
#Create ability to perform operation
#Create return statement

class PyCreate():

    reader = JSON()
    
    def create_function(self, name, param_name, operation, file):
        indent = "   "
        new_line = "\n"
        line = self.reader.getData("py", "function", "code")
        line = line.replace("<name>", name)
        params = []
        for p_name in param_name:
            param = self.create_param(True, p_name)
            params.append(param)
        param = ''
        count = 0
        for p in params:
            count += 1
            if count < len(params):
                param += (p + ", ")
            else:
                param += (p)
            
        line = line.replace("<param>", param)
        line_two = self.create_body(operation, params)
        line_three = self.create_return(operation)
        text = line + new_line + indent + line_two + new_line + indent + line_three

        self.write_line(file, text)
        
    def create_param(self, func_param, name, value = "[]"):
        param = name
        if not func_param:
            param = name + " = " + value
        return param
            
    def create_body(self, operation, variables):
        line = self.reader.getData("py", "functions", operation)
        line = line["code"]
        count = 0
        for var in variables:
            count += 1
            line = line.replace("<var" + str(count) + ">", var)
        return line
    
    def create_return(self, operation):
        line = self.reader.getData("py", "functions", operation)
        line = line["return"]
        return line
    
    def get_indent(self):
        indent = "   "
        return indent

    def get_new_line(self):
        new_line = "\n"
        return new_line
    
    def create_print(self, text):
        print_b = self.reader.getData("py", "print", "beginning")
        print_e = self.reader.getData("py", "print", "end")

        line = print_b + text + print_e

        return line
    
    def create_app_run_multi(self):
        line = self.reader.getData("py", "run")
        return line
    
    def create_app_run_single(self, call, params, file):
        indent = "   "
        new_line = "\n"
        line = self.reader.getData("py", "run")
        line_two = call
        count = 0
        print_b = self.reader.getData("py", "print", "beginning")
        print_e = self.reader.getData("py", "print", "end")
        for p in params:
            count += 1
            if count < len(params):
                line_two += (p + ", ")
            else:
                line_two += (p)
        text = new_line + new_line + line + new_line + indent + print_b + line_two + print_e + print_e
        self.write_line(file, text)
            
    def write_line(self, file, text):
        with open(file, 'a') as f:
            f.write(text)
            
    def create_import(self, name):
        line = self.reader.getData("py", "import")
        line = line.replace("<name>", name)
        return line
    
    def create_call(self, name, params):
        line = self.reader.getData("py", "call", "beginning")
        line = line.replace("<name>", name)
        count = 0
        for param in params:
            count += 1
            if count < len(params):
                line += (param + ",")
            else:
                line += param
        line += self.reader.getData("py", "call", "end")
        return line
        
    def call_py(self, file):
        test = subprocess.run("python " + file,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              check=True,
                              text=True,
                              shell=True)
        return test.stdout

if __name__ == '__main__':
    pass
