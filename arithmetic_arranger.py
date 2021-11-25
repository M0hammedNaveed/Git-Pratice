

def arithmetic_arranger(x,val=False):
    if len(x)>5:
        print("Error: Too many problems.")
        quit()        
    up=[]
    down=[]
    sol=[]
    for a in x:
        a=a.split()
        if a[1]=='/'or a[1]=='*':
            print("Error: Operator must be'+' or '-'.")
            quit()
        elif a[1] !='-':
            if a[1] !='+':
                print("Error: Numbers must only contain digits")
                exit()
        try:
            up.append(' '), up.append(int(a[0])), 
            down.append(a[1]), down.append(int(a[2]))
            if a[1]=='-':
                sol.append(' '), sol.append(int(a[0])-int(a[2]))
            elif a[1]=='+':
                sol.append(' '), sol.append(int(a[0])+int(a[2]))
        except:
            print("Error: Numbers must only contain digits.")
            quit()
        if len(a[0])>4 or len(a[2])>4:
            print("Error: Numbers cannot be more than four digits.")
            quit()
        
    if len(x)==5: 
        print('%s%5d %s %s%5d %s %s%5d %s %s%5d %s %s%5d'%(up[0],up[1],'  ',up[2],up[3],'  ',up[4],up[5],'  ',up[6],up[7],'  ',up[8],up[9]))
        print('%s%5d %s %s%5d %s %s%5s %s %s%5d %s %s%5d'%(down[0],down[1],'  ',down[2],down[3],'  ',down[4],down[5],'  ',down[6],down[7],'  ',down[8],down[9]))
        print('%s%5s %s %s%5s %s %s%5s %s %s%5s %s %s%5s'%('-','-----',' ',' -','-----',' ',' -','-----',' ',' -','-----',' ',' -','-----'))
    if len(x)==4:
        print('%s%5d %s %s%5d %s %s%5d %s %s%5d'%(up[0],up[1],'  ',up[2],up[3],'  ',up[4],up[5],'  ',up[6],up[7]))
        print('%s%5d %s %s%5d %s %s%5s %s %s%5d'%(down[0],down[1],'  ',down[2],down[3],'  ',down[4],down[5],'  ',down[6],down[7]))
        print('%s%5s %s %s%5s %s %s%5s %s %s%5s'%('-','-----',' ',' -','-----',' ',' -','-----',' ',' -','-----'))
    if len(x)==3:
        print('%s%5d %s %s%5d %s %s%5d'%(up[0],up[1],'  ',up[2],up[3],'  ',up[4],up[5]))
        print('%s%5d %s %s%5d %s %s%5s'%(down[0],down[1],'  ',down[2],down[3],'  ',down[4],down[5]))
        print('%s%5s %s %s%5s %s %s%5s'%('-','-----',' ',' -','-----',' ',' -','-----'))
    if len(x)==2:
        print('%s%5d %s %s%5d'%(up[0],up[1],'  ',up[2],up[3]))
        print('%s%5d %s %s%5d'%(down[0],down[1],'  ',down[2],down[3]))
        print('%s%5s %s %s%5s'%('-','-----',' ',' -','-----'))
    if len(x)==1:
        print('%s%5d'%(up[0],up[1]))
        print('%s%5d'%(down[0],down[1]))
        print('%s%5s'%('-','-----'))





    if val==True and len(x)==5:
        print('%s%5d %s %s%5d %s %s%5d %s %s%5d %s %s%5d'%(sol[0],sol[1],'  ',sol[2],sol[3],'  ',sol[4],sol[5],'  ',sol[6],sol[7],'  ',sol[8],sol[9]))
    if val==True and len(x)==4:
        print('%s%5d %s %s%5d %s %s%5d %s %s%5d'%(sol[0],sol[1],'  ',sol[2],sol[3],'  ',sol[4],sol[5],'  ',sol[6],sol[7]))
    if val==True and len(x)==3:
        print('%s%5d %s %s%5d %s %s%5d'%(sol[0],sol[1],'  ',sol[2],sol[3],'  ',sol[4],sol[5]))
    if val==True and len(x)==2:
        print('%s%5d %s %s%5d'%(sol[0],sol[1],'  ',sol[2],sol[3]))
    if val==True and len(x)==1:
        print('%s%5d'%(sol[0],sol[1]))


arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "345 + 123"], True)
       


