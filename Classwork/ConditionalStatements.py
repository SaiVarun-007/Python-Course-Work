###Example1###

items=['shoes','smartwatch','phone','laptop','airpods','toycar'] 
print ('Relcome to Amazon store'.center (50,'s')) 
searchinput=input ("Enter the item:").lower ()
if searchinput in items:
    print (f"(searchinput) found. Buy now!!!") 
else:
    print (f" (searchinput) is out of stock now. we will notify you.")


###Example1###

#Weekend Budget Plan 

amount=int(input("Enter the amount you can spend for weekend: ") )

if amount>20000:
    print ("Trip to Goa")
elif amount>15000:
    print ("Go for Shopping") 
elif amount>10000:
    print ("Clublingg")
elif amount>5000:
    print ("Cafe/Dinner") 
elif amount>2000:
    print ("Maintancesss")
elif amount>500:
    print ("Go for movie")
elif amount>100:
    print ("Go for street food")
else:
    print ("Save the money and sleep")
    

###Example1###

#Grading System

data={
    1:{'name':'praveen','attempt_status':False,'python':0,'sql':0,'powerbi':0},
    2:{'name':'Harshith','attempt_status':True,'python':100,'sql':90,'powerbi':80},
    3:{'name':'Varun','attempt_status':True,'python':70,'sql':90,'powerbi':50},
    4:{'name':'Tarit','attempt_status':True,'python':30,'sql':100,'powerbi':25},
    5:{'name':'Sheshu','attempt_status':True,'python':60,'sql':40,'powerbi':35},
}

stuid=int(input("Enter the student id: "))

if data[stuid]['attempt_status']:
    total=(data[stuid]['python']+data[stuid]['sql']+data[stuid]['powerbi'])/3
    if total>90:
        print(f'Congrats!!!\n{data[stuid]["name"]} got "A" grade')
    elif total>75:
        print(f'Good!!!\n{data[stuid]["name"]} got "B" grade')
    elif total>50:
        print(f'Try it improve!!!\n{data[stuid]["name"]} got "C" grade')
    elif total>35:
        print(f'Just Passed!!!\n{data[stuid]["name"]} got "D" grade')
    else:
        print(f'Better luck next time!!!\n{data[stuid]["name"]} failed')
        
else:
    print(f'{data[stuid]["name"]} is not attempted the exam.')