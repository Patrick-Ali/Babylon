import subprocess
from TextAnalysis import TextAnalysis as TA
import requests

def get_last():
    
    request = requests.get('http://api.open-notify.org')
    print(request.text)
    
    ta = TA()
    last = subprocess.run("git rev-parse HEAD",
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              check=True,
                              text=True,
                              shell=True)
    out = last.stdout
    head = subprocess.run("git cat-file -p " + out,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              check=True,
                              text=True,
                              shell=True)
    hold = head.stdout
    h_array = ta.tokenize_sentence(hold)
    tree = h_array[1]
    parent = h_array[3]
    print(hold)
    print(h_array)
    #git cat-file -p output
    #6c9a575d965cab33217d249b335cd03c8817fcff
if __name__ == '__main__':
    get_last()
