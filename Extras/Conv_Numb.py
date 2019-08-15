import re

from JSON import JSON as js
from TextAnalysis import TextAnalysis as ta

def add(num1, num2):
    
    num3 = num1 + num2
    return num3
def multi(num1, num2):
    
    num3 = num1 * num2
    return num3

def getNum(num, last_num, cur_num, extra, last, next_num):
    '''Determine the numbers in the sentence'''
    data = js()
    nums = data.loadData("numbers")
    
    words = ["hundred","thousand","million","billion","trillion"]
    
    for element in nums:
        
        if nums[element] == num.lower() or element == num:

            
            
            multis = ["00","000","000000","000000000","000000000000"]
 
            if element in multis:
                numb = cur_num
                multi_now = False
                if numb == 0:
                    numb = last
                    cur_num = last
                    
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
                if extra != 0: 
                    if extra == cur_num:
                        numb = numb
                    elif (num in words and next_word not in words or num not in words and next_word not in words or num not in words and next_word in words):#elif (num in words and next_num not in words or num not in words and next_num not in words or num not in words and next_num in words):
                        
                        numb = add(numb, extra)
                    
                    else:
                        numb = extra
                return (numb, 1, last)
            numb = int(element)
            
            if last_num:
                numb = add(numb, cur_num)
            return (numb, 0)
    print(extra)
    if extra > 0:
        return (extra + cur_num, 3)
    return "Unknown Number"

def regexe(text):
    #x = re.findall("[1-9]x+", text)
    #y = re.findall("\d+\sx{1}", text)
    #hold = Conv_Numb.regexe("I want a program to add 12345 variables together.")
    z = re.findall("\d+\svariables{1}", text) 
    return z

if __name__ == "__main__":
    hold = ta()
    #hold = Conv_Numb.regexe("I want a program to add 12345 variables together.")
    temp = hold.tokenize_sentence("I want a program to add one million two hundred thousand thirty thousand four thousand five hundred sixty seven variables together")
    print(temp)
    #temp = hold.tokenize_sentence("I want a program to add one trillion trillion trillion two hundred billion thirty four billion five hundred million sixty seven million eight hundred thousand ninety one thousand two hundred thirty four numbers togther.")
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
    start_num = -1
    final = 0
    for word in temp:
        if count+1 < len(temp):
            next_word = temp[count+1]
        else:
            next_word = ""
        num = getNum(word,last_num,cur_num, extra, last, next_word)
        if num != "Unknown Number":
            start_num += 1
            
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
            
            
            count += 1
            final = num[0]
            continue
        elif num == "Unknown Number":
            last_num = False
            cur_num = 0
            count += 1
            if start_num != -1:
                temp[count - (start_num+2)] = final
                if (count - (start_num+2)) + 1 < len(temp):

                    del temp[(count - (start_num+2)+1):(count-2)]
                    start_num = -1
    print(temp)

    holding = " ".join(str(e) for e in temp)

    print(holding)
            
    #print(regexe("I want a program to add 12345 x numbers togther."))

    print(regexe(holding))
