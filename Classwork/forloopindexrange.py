s='Varun Praveen Rasool Chaitanya Tarit'
n=len(s)
ch=input("Enter the char: ").lower()

for i in range(n):
    if s[i]==ch:
        print(ch, i)
