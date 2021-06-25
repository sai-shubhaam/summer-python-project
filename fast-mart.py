items_dict={'1':'Apple', '2':'Orange','3':'Banana', '4':'Guava','5':'Mango',
'6' : 'Peach','7':'Ladies Finger','8':'Peas','9':'Carrot','10':'Radish',
'11':'Broccoli','12':'Mushroom','13':'Maggie','14':'Lays', '15':'Doritos',
'16':'Pringles','17':'Oreos','18':'Bourbon','19':'Coke','20':'Pepsi','21':'Frooti',
'22':'Maaza','23':'Mountain Dew','24':'Milk','25':'Cheese','26':'Curd','27':'Dairy Milk',
'28':'Baguette','29':'Croissant','30':'Hard Bread','31':'Sour Dough Bread','32':'Multi Grain Bread','33':'Soulfull',
'34':'Corn Flakes','35':'Chocos'}
bought_together_sets= [{'1','2','3'},
{'4','5','6'}]
keep_running_loop="Y"
user_choice=1
price_dict={"1":10,"2":30,"3":25,"4":15, "5": 35, "6": 30}
total_price = 0
cart = []

print("welcome to Fast Mart!")
while(keep_running_loop=="Y"):
    print("TODO: print entire menu")
    user_choice = input("Please pick an item!")
    if(user_choice not in items_dict.keys()):
        print("Hmm, this seems to be an invalid choice!")
        continue
    cart.append(items_dict[user_choice])
    print("Items currently in your cart are: ", cart)
    total_price = total_price + price_dict[user_choice]
    for sets in bought_together_sets:
        if(user_choice in sets):
            print("Users who bought "+items_dict[user_choice]+" also bought:")
            for item in sets:
                if(item!=user_choice):
                    print(items_dict[item])
    keep_running_loop=input("Add more items? Y for yes, N for no.")

print("Thanks for shopping with Fast Mart! Your total is",total_price)
     
    
            