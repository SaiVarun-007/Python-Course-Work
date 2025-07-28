def display(s, ind):
    if ind==-1:
        return 
    print (s[ind], end='')
    display(s, ind -1)
    
s='python programming'
display(s,len(s)-1)