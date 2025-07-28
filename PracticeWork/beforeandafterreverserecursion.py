def display(s,ind): 
    if ind==len(s): 
        return
    
    print("Before:",s[ind],end='\t') 
    display(s,ind+1) 
    print("After:",s[ind],end='\t')


s='Python programming'
display(s,0)