from JSON import JSON

import subprocess
class PyCreate():

    reader = JSON()
    
    def create_function(self, name, param_name, operation, file, count, ret, extra_text, sample_params, var_count, para_count): #, extra
        indent = "   "
        new_line = "\n"
        line = ""
        params = []
        
        if count == 1:
            line = self.reader.getData("py", "function", "code")
            line = line.replace("<name>", name)
            for p_name in param_name:
                if p_name != "param_empty":
                    param = self.create_param(True, p_name)
                    params.append(param)
            param = ''
            count_param = 0
            for p in params:
                count_param += 1
                if count_param < len(params):
                    param += (p + ", ")
                else:
                    param += (p)
            line = line.replace("<param>", param)
        
        else:
            start = var_count - para_count
            count_param = 1
            line = new_line + indent
            while count_param <= para_count:
                if start < len(sample_params):
                    temp = sample_params[start]
                    if temp == 'ans':
                        params.append("hold"+str((count-1)))
                    else:
                        params.append(param_name[start])
                    start += 1
                    count_param += 1
        line_two = self.create_body(operation, params)
        line_three = ''
        if ret == True:
            line_three = self.create_return(operation)
            text = ""
            if extra_text != "":
                text = extra_text + line + new_line + indent + line_two + new_line + indent + line_three + new_line + new_line#"#New Line Test"
            else:
                text = line + new_line + indent + line_two + new_line + indent + line_three + new_line + new_line#"#New Line Test"
            return text
        else:
            line_three = self.get_answer(operation, count)
            text = ""
            if extra_text != "":
                text = extra_text + line + new_line + indent + line_two + new_line + indent + line_three
            else:
                text = line + new_line + indent + line_two + new_line + indent + line_three
            return text
                
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
    
    def get_answer(self, operation, count):
        line = self.reader.getData("py", "functions", operation)
        line = "hold"+str(count)+" = "+line["name"]
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
    
    def py_version(self):
        test = subprocess.run("python --version",
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              check=True,
                              text=True,
                              shell=True)

        ver = 7
        if len(test.stdout) == 13:
            ver = 7
        elif len(test.stdout) == 11:
            ver = 6
        elif len(test.stdout) == 9:
            ver = 5
        return test.stdout[ver] 
        
    def call_py(self, file):
        version = self.py_version()
        if version == '3':
            test = subprocess.run("python " + file,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              check=True,
                              text=True,
                              shell=True)
            return test.stdout
        
        else:
            test = subprocess.run("python3 " + file,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  check=True,
                                  text=True,
                                  shell=True)
            return test.stdout

if __name__ == '__main__':
    pass
