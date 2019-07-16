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

def getNum(num, last_num, cur_num, extra, last, next_num):
    '''Determine the numbers in the sentence'''
    data = js()
    nums = data.loadData("numbers")
    print("Extra: " + str(extra))
    words = ["hundred","thousand","million","billion","trillion"]
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
                multi_now = False
                if numb == 0:
                    numb = last
                    cur_num = last
                    print("Last: " + str(last))
                if element == "00":
                    numb = multi(cur_num, 100)
                    multi_now = True
                elif element == "000":
                    numb = multi(cur_num, 1000)
                    multi_now = True
                elif element == "000000":
                    numb = multi(cur_num, 1000000)
                    multi_now = True
                elif element == "000000000":
                    numb = multi(cur_num, 1000000000)
                    multi_now = True
                elif element == "000000000000":
                    numb = multi(cur_num, 1000000000000)
                    multi_now = True
                last_num = False
                last = numb
                if extra != 0: #and jump == False:
                    print("Hello " + str(numb))
                    #last = numb
                    #if jump == False:
                    print("Num " + num)
                    print("Next Word " + next_word)
                    if extra == cur_num:
                        numb = numb
                    elif (num in words and next_word not in words or num not in words and next_word not in words or num not in words and next_word in words): #and extra != cur_num: #: #and multi_now == False
                        print("Cur num " + str(cur_num))
                        numb = add(numb, extra)
                    #elif multi_now == False:
                    else:
                        numb = extra
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
    #Track sequence
    #1,234,567,890
    #1,234,567,890
    #1,234,567,891,234
    #temp = hold.tokenize_sentence("I want a program to add one million two hundred thousand thirty thousand four thousand five hundred sixty seven numbers togther.")
    temp = hold.tokenize_sentence("I want a program to add one trillion trillion trillion two hundred billion thirty four billion five hundred million sixty seven million eight hundred thousand ninety one thousand two hundred thirty four numbers togther.")
    #temp = hold.tokenize_sentence("I want a program to add one hundred thousand three numbers togther.")
    #temp = hold.tokenize_sentence("I want a program to add one trillion")
    last_num = False
    cur_num = 0
    extra = False
    last = 0
    next_word = ""
    words = ["hundred","thousand","million","billion","trillion"]
    jump = False
    count = 0
    for word in temp:
        if count+1 < len(temp):
            next_word = temp[count+1]
        else:
            next_word = ""
        #if word in words and next_word in words:
            #jump = True
        #elif next_word not in words:
            #jump = False
        num = getNum(word,last_num,cur_num, extra, last, next_word)
        if num != "Unkown Number":
            #last_word = word
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
            count += 1
            continue
        elif num == "Unkown Number":
            last_num = False
            cur_num = 0
            count += 1
            
    print(regexe("I want a program to add 12345 x numbers togther."))
