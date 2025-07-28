def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s, ind+1)
    
s='python programming'
display(s,0)
