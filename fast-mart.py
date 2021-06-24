items_dict={'1':'milk', '2':'eggs','3':'bread', '4':'coke','5':'pizza', '6' : 'galic bread'}
bought_together_sets= [{'1','2','3'},
{'4','5','6'}]
keep_running_loop=True
user_choice=1

# TODO: Price and final bill
# TODO: Give the option to buy any of the items suggested

while(keep_running_loop):
    print("welcome to Fast Mart!")
    print("TODO: print entire menu")
    user_choice = input("Please pick an item!")
    for sets in bought_together_sets:
        if(user_choice in sets):
            print("Users who bought "+items_dict[user_choice]+" also bought "+str(sets))