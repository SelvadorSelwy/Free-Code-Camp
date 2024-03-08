import re


def arithmetic_arranger(arirhmetic_problems, show_answer=False):

    # a is first part of the problem, b is second part and c is the operater in the problem

    try:
        if len(arirhmetic_problems)> 5 :
            raise Exception('Error: Too many problems.')
            
        alist=[]
        blist=[]
        operators_list=['+', '-']
        answers_list = []
     
        for problem in arirhmetic_problems:
            a = re.findall('\S+\s', problem)[0].strip()
        
            if problem.find('+') != -1:
                plus_pos= problem.find('+') 
            else: plus_pos= problem.find('-')
    
            b = problem[plus_pos+1:].strip()
            
            if not a.isdigit() or not b.isdigit():
                raise Exception('Error: Numbers must only contain digits.')
            elif len(a) > 4 or len(b) > 4:
                raise Exception('Error: Numbers cannot be more than four digits.')

            c = re.findall("\s\S\s", problem)[0].strip()
            if c not in operators_list:
                raise Exception("Error: Operator must be '+' or '-'.")

            answer = int(a)+int(b) if c == "+" else int(a)-int(b)
            
            if len(a) > len(b):
                c= c+' '
                a= a.rjust(len(a)+ len(c)," ")
                b= c+ b.rjust(len(a)-len(c), " ")
                answer= str(answer).rjust(len(a)," ")
            else:
                c= c+' '
                a= a.rjust(len(b)+ len(c)," ")
                b= c+ b
                answer= str(answer).rjust(len(b))

            alist.append(a)
            blist.append(b)
            answers_list.append(answer)

        for i in range(len(alist)):
            print(alist[i], end="    " if i < len(alist)-1 else "\n")
        for i in range(len(alist)):
            print(blist[i], end="    " if i < len(alist)-1 else "\n")
        for i in range(len(alist)):
            print("-"* len(alist[i]), end="    " if i < len(alist)-1 else "\n")
        if show_answer:
            for i in range(len(alist)):
                print(answers_list[i], end="    " if i < len(alist)-1 else "\n")
        else:print()
    except Exception as e:
        print(e.args[0])

    
arithmetic_arranger(["8566 + 54", "718 + 9584", "2645 - 2825", "4251 + 63", "5 - 825"], True)
