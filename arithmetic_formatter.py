import re

solve = True
problems = ["32 + 6982", "3801 - 2", "45 + 43", "123 + 49", "9999 + 9999"]

if len(problems) > 5:
    print('Error: Too many problems.')
    quit()

Line1 = Line2 = Line3 = Line4 = ''

for problem in problems:
    if re.search("[^\s0-9+-]", problem):
        if re.search("[*]", problem) or re.search("[/]", problem):
            print("Error: Operator must be '+' or '-'.")
            quit()
        else:
            print('Numbers must only contain digits.')
            quit()

    operand1 = problem.split()[0]
    operator = problem.split()[1]
    operand2 = problem.split()[2]

    if len(operand1) > 4 or len(operand2) > 4:
        print('Error: Numbers cannot be more than four digits.')
        quit()

    longOp = max(len(operand1), len(operand2))
    probLength = longOp + 2

    line1 = (operand1).rjust(probLength) + ' ' * 4
    if len(operand2) > len(operand1):
        line2 = (operator + ' ' + operand2).rjust(probLength) + ' ' * 4
    else:
        line2 = (operator + ' ' * (len(operand1) - len(operand2) + 1) + operand2).rjust(probLength) + ' ' * 4
    line3 = '-' * (probLength) + ' ' * 4

    if operator == '+':
        line4 = str(int(operand1) + int(operand2)).rjust(probLength) + 4*' '
    else: line4 = str(int(operand1) - int(operand2)).rjust(probLength) + 4*' '

    Line1 += line1
    Line2 += line2
    Line3 += line3
    Line4 += line4

if solve:
    arranged_problems = (Line1.rstrip() + '\n' + Line2.rstrip() + '\n' + Line3.rstrip() + '\n' + Line4.rstrip())
else:
    arranged_problems = (Line1.rstrip() + '\n' + Line2.rstrip() + '\n' + Line3.rstrip())


print(arranged_problems)
