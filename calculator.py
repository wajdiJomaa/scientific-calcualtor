from math import factorial
from math import e
from math import pi
from math import cos
from math import sin
from math import radians

def pre_parse(exp):
    if exp[0] == '+' or exp[0] == '-':
        return parse('0'+ exp)
    return parse(exp)

def parse(exp):
    parentheses = 0
    add = -1
    minus = -1
    mult = -1
    div = -1
    power = -1
    radical = -1
    facto = -1
    virgule = -1
    modulo = -1
    sinus = -1
    cosinus = -1

    for i in range(len(exp)) :
        
        if exp[i] == '(' : 
            parentheses += 1
            continue
        elif exp[i] == ")":
            parentheses -= 1
            continue
        
        if parentheses == 0:
            if exp[i] == "+":
                add = i  
            
            if exp[i] == "*":
                mult = i  
            
            if exp[i] == "-":
                minus = i  
            
            if exp[i] == "/":
                div = i 
            
            if exp[i] == "^":
                power = i
            
            if exp[i] == "#":
                radical = i

            if exp[i] == "!":
                facto = i
            
            if exp[i] == ",":
                virgule = i

            if exp[i] == "%":
                modulo = i
            
            if exp[i] == "s":
                sinus = i
            
            if exp[i] == "c":
                cosinus = i

    if add > 0:
        left = parse(exp[0:add]) 
        right = parse(exp[add+1::])
        return ["+",left,right]
    
    if minus > 0:
        left = parse(exp[0:minus]) 
        right = parse(exp[minus+1::])
        return ["-",left,right]
    
    if mult > 0:
        left = parse(exp[0:mult]) 
        right = parse(exp[mult+1::])
        return ["*",left,right]
    
    if div > 0:
        left = parse(exp[0:div]) 
        right = parse(exp[div+1::])
        return ["/",left,right]
    
    if modulo > 0:
        left = parse(exp[0:modulo]) 
        right = parse(exp[modulo+1::])
        return ["%",left,right]
    
    if power > 0:
        left = parse(exp[0:power]) 
        right = parse(exp[power+1::])
        return ["^",left,right]

    if radical > 0:
        left = parse(exp[0:radical]) 
        right = parse(exp[radical+1::])
        return ["#",left,right]

    if sinus >= 0:
        right = parse(exp[sinus+1::])
        return ["s",right]
    
    if cosinus >= 0:
        right = parse(exp[cosinus+1::])
        return ["c",right]

    if facto > 0:
        left = parse(exp[0:facto]) 
        return ["!",left]

    if virgule > 0:
        left = parse(exp[0:virgule]) 
        right = parse(exp[virgule+1::])
        return [",",left,right]

    if (exp[0]=="("):
        return parse(exp[1:(len(exp)-1)])

    return exp

def evaluate(exp):
    if not isinstance(exp,list):
        if (exp.strip() == "e"):
            return e
        if (exp.strip() == "pi"):
            return pi
        
        return int(exp)
        

    left = evaluate(exp[1])
    
    if exp[0] == "!":
        return factorial(left)
    
    if exp[0] == 'c':
        return cos(radians(left))
    
    if exp[0] == 's':
        return sin(radians(left))
    
    right = evaluate(exp[2])

    if exp[0] == '+':
        return left + right
    if exp[0] == '*':
        return left * right
    if exp[0] == '-':
        return left - right
    if exp[0] == '/':
        return left / right
    if exp[0] == '^':
        return left**right 
    if exp[0] == '#':
        return right ** (1/left)
    if exp[0] == ',':
        return left + right/(10*len(str(right)))
    if exp[0] == '%':
        return left % right

def print_exe(exp,level=0) :
    if not isinstance(exp,list):
        print(level*"  ",end="")
        print(exp.strip())
        return
    
    print(level*"  ",end="")
    print(exp[0].strip())
    print_exe(exp[1],(level+1))
    
    if (len(exp) == 2):
        return    
    
    
    print_exe(exp[2],(level+1))
    return

def main(exp):
    prs = pre_parse(exp)
    print("\nexpression:")
    print(exp)
    print("\nparse: ")
    print(prs)
    print("\ntree: ")
    print_exe(prs)
    print("\nresult = ",end="")
    print(evaluate(prs))

main("2#(s20^2 + c20^2)")
