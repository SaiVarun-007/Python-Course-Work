grocery_items = {
    1:{"Name":"Rice", "Price": 60},
    2:{"Name":"Wheat Flour", "Price": 25},
    3:{"Name":"Sugar", "Price": 40},
    4:{"Name":"Milk", "Price": 30},
    5:{"Name":"Eggs (12 pcs)", "Price": 60},
    6:{"Name":"Cooking Oil", "Price": 130},
    7:{"Name":"Tea Powder", "Price": 90},
    8:{"Name":"Salt", "Price": 30},
    9:{"Name":"Bread", "Price": 40},
    10:{"Name":"Sopa", "Price": 40}
}

for i in grocery_items:
    print(f'{i}. {grocery_items[i]["Name"]} - $ {grocery_items[i]["Price"]}')

items = list(map(int,input("Enter The Product Indexes(1 2 3 4 5): ").split()))

total=0
s=set()
for i in items:
    if i not in s:
        c=items.count(i)
        print(f'{grocery_items[i]["Name"]}-{c}*${grocery_items[i]["Price"]}=${c*grocery_items[i]["Price"]}')
        total+=grocery_items[i]["Price"]*c
        s.add(i)
print(f"Total Bill: {total}")
