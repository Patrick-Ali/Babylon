import re

from JSON import JSON as js
from TextAnalysis import TextAnalysis as ta

def add(num1, num2):
    print("Add " + str(num1))
    print("Add " + str(num2))
    num3 = num1 + num2
    return num3
def multi(num1, num2):
    print("Multi " + str(num1))
    print("Multi " + str(num2))
    num3 = num1 * num2
    return num3

def getNum(num, last_num, cur_num, extra, last):
    '''Determine the numbers in the sentence'''
    data = js()
    nums = data.loadData("numbers")
    print("Extra: " + str(extra))
    #print(num.lower())
    for element in nums:
        #print(element)
        #print(element == num)
        if nums[element] == num.lower() or element == num:
            #print("Working")
            #print(nums[element])
            
            print("Original " + element)
            multis = ["00","000","000000","000000000","000000000000"]
            print("Cur " + str(cur_num))
            #last = 0
            if element in multis:
                numb = cur_num
                if numb == 0:
                    numb = last
                    cur_num = last
                    print("Last: " + str(last))
                if element == "00":
                    numb = multi(cur_num, 100)
                elif element == "000":
                    numb = multi(cur_num, 1000)
                elif element == "000000":
                    numb = multi(cur_num, 1000000)
                elif element == "000000000":
                    numb = multi(cur_num, 1000000000)
                elif element == "000000000000":
                    numb = multi(cur_num, 1000000000000)
                last_num = False
                if extra != 0:
                    print("Extra ")
                    last = numb
                    numb += extra
                return (numb, 1, last)
            numb = int(element)
            print("Before " + str(num))
            print("After " + str(numb))
            #print("Cur " + str(cur_num))
            #multis = ["000","0000","000000","000000000","000000000000"]
##            if str(cur_num) in multis:
##                if cur_num == 000:
##                    numb = multi(numb, 100)
##                elif cur_num == 0000:
##                    numb = multi(numb, 10000)
##                elif cur_num == 000000:
##                    numb = multi(numb, 1000000)
##                elif cur_num == 000000000:
##                    numb = multi(numb, 1000000000)
##                elif cur_num == 000000000000:
##                    numb = multi(numb, 1000000000000)
##                last_num = False
            if last_num:
                numb = add(numb, cur_num)
            return (numb, 0)
    if extra > 0:
        return (extra + cur_num, 3)
    return "Unkown Number"

def regexe(text):
    x = re.findall("[1-9]x+", text)
    y = re.findall("\d+\sx{1}", text) 
    return (x, y)

if __name__ == "__main__":
    hold = ta()
    temp = hold.tokenize_sentence("I want a program to add one million two hundred thousand thirty thousand four thousand five hundred sixty seven numbers togther.")
    last_num = False
    cur_num = 0
    extra = False
    last = 0
    for word in temp:
        num = getNum(word,last_num,cur_num, extra, last)
        if num != "Unkown Number":
            last_num = True
            extra_true = num[1]
            if extra_true == 3:
                extra_true = False
                last_num = False
                cur_num = 0
                extra = 0
                
            elif extra_true:
                cur_num = 0
                extra = num[0]
                last = num[2]
            else:
                cur_num = num[0]
            
            print(num)
            continue
        elif num == "Unkown Number":
            last_num = False
            cur_num = 0
            
    print(regexe("I want a program to add 12345 x numbers togther."))
