items_dict={'1':'Apple', '2':'Orange','3':'Banana', '4':'Guava','5':'Mango',
'6' : 'Peach','7':'Ladies Finger','8':'Peas','9':'Carrot','10':'Radish',
'11':'Broccoli','12':'Mushroom','13':'Maggie','14':'Lays', '15':'Doritos',
'16':'Pringles','17':'Oreos','18':'Bourbon','19':'Coke','20':'Pepsi','21':'Frooti',
'22':'Maaza','23':'Mountain Dew','24':'Milk','25':'Cheese','26':'Curd','27':'Dairy Milk',
'28':'Baguette','29':'Croissant','30':'Hard Bread','31':'Sour Dough Bread','32':'Multi Grain Bread','33':'Soulfull',
'34':'Corn Flakes','35':'Chocos'}
bought_together_sets= [{'1','2','3'},
{'4','5','6'},
{'7','8','9'},
{'10','11','12'},
{'13','14','15'},
{'16','17','18'},
{'20','21','22'},
{'24','25','26'},
{'27','28','29'},
{'30','31','32'},
{'33','34','35'}]

keep_running_loop="y"
user_choice=1
price_dict={"1":5,"2": 10,"3":20,"4":20, "5": 10, "6":10, "7": 20, "8":20, "9": 30, "10": 35, "11": 40, "12": 20, "13": 10, "14": 10, "15": 20, 
"16": 10, "17": 10, "18": 15, "19": 15, "20":35, "21":10, "22":10, "23":15, "24":25, "25": 15, "26":25, "27": 5, "28": 55, "29":50, "30": 45, 
"31": 35, "32": 25, "33": 20, "34": 20, "35": 20,}
total_price = 0
cart = []

print("welcome to Fast Mart!")
while(keep_running_loop=="y"):
    for item in items_dict.keys():
        print(item,": ",items_dict[item])
    user_choice = input("Please pick an item! \n")
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
                    print(items_dict[item]," Product Code: ",item)
    keep_running_loop=input("Add more items? y for yes, n for no.")

print("Thanks for shopping with Fast Mart! Your total is ",total_price, " rupees.")
     
    
            