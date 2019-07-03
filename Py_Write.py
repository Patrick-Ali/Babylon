from JSON import JSON

import subprocess


def test(file, text):
    with open(file, 'a') as f:
        f.write(text)
        #f.write('print("Hello World")')
def test_call():
    test = subprocess.run("python test2.py",
    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    check=True,
    text=True,
    shell=True)

    print(test.stdout)

if __name__ == '__main__':
    indent = "   "
    new_line = "\n"
    test_call()
    #reader = JSON()
    #line = reader.getData("py", "run")
    #test("test2.py", line + new_line)
    #line1 = reader.getData("py", "print", "beginning")
    #line2 = '"Hello World"'
    #line3 = reader.getData("py", "print", "end")
    #sentence = indent + line1 + line2 + line3 + new_line
    #test("test2.py", sentence)
    #test("test2.py")
