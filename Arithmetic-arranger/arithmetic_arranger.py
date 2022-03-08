
def arithmetic_arranger(problems, display=False):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    countProblems = len(problems)
    if countProblems>5 :
        return "Error: Too many problems."
    iteration = 0
    for problem in problems:
        string = problem.split(" ")
        #find the highest digit count
        maxDigits = len(string[0]) if len(string[0]) > len(string[2]) else len(string[2]) 
        if maxDigits>4:
            return "Error: Numbers cannot be more than four digits."

        try:
            num1 = int(string[0])
            num2 = int(string[2])
        except:
            return "Error: Numbers must only contain digits." 
        if string[1] == "+":
            answer = num1+num2
        elif string[1] == "-":
            answer = num1-num2
        else:
            return "Error: Operator must be '+' or '-'."
        #padding
        for i in range((maxDigits+2)-len(string[0])):
            line1 += " "
        line2+=string[1]
        for i in range((maxDigits+1)-len(string[2])):
            line2 += " "
        for i in range(maxDigits+2):
            line3 += "-"
        for i in range((maxDigits+2)-len(str(answer))):
            line4 += " "
        #add the numbers
        line1 += string[0]
        line2 += string[2]
        line4 += str(answer)
        iteration+=1
        #add 4 spaces if there is more than 1 problem
        if countProblems > 1 and iteration != countProblems:
            line1+="    "
            line2+="    "
            line3+="    "
            line4+="    "
    if display == True:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    else:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3
    return arranged_problems

        
print(arithmetic_arranger(['98 + 35', '3801 - 2', '45 + 43', '123 + 49'], True))
