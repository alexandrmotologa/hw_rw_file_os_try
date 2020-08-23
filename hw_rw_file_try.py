from os.path import exists

my_menu = "menu.txt"
client_order = "order.txt"

list_of_menu = []
list_of_order = []

if exists(my_menu) and exists(client_order):
    print(f"\nNEW ORDER FOUND!\n\n")
    client_order = open(client_order, "r")
    my_menu = open(my_menu, "r")
    for line in my_menu:
        stripped_line = line.strip()
        line_list = stripped_line.split("|")
        list_of_menu.append(line_list)
    for line in client_order:
        stripped_line = line.strip()
        line_list = stripped_line.split("|")
        list_of_order.append(line_list)
else:
    print("ERROR...NO FILE...")


# sortarea listelor

def sort_list(my_list):
    for j in range(len(my_list)):
            for i in range(len(my_list) - 1):
                if my_list[i][0] > my_list[i + 1][0]:
                    temp = my_list[i]
                    my_list[i] = my_list[i + 1]
                    my_list[i + 1] = temp

sort_list(list_of_menu)
sort_list(list_of_order)

total = []
try:
    for i in range(len(list_of_menu)):
        if list_of_menu[i][0] == list_of_order[i][0] or list_of_menu[i][0] != list_of_order[i][0]:
            name = list_of_order[i][0:1]
            name = str(*name)
            quantity = list_of_order[i][1]
            quantity = float(quantity)
            price_piece = list_of_menu[i][3]
            price_piece = float(price_piece)
            a = quantity * price_piece
            total.append(a)
            weight = list_of_menu[i][2]
            weight = float(weight)
            print(f"Name: {name:30s} Quantity: {quantity:^10.1f} Weight: {quantity * weight:>8.3f} gr. Price: {a:^10.1f} {list_of_menu[i][4]}")
except:
    print(f'\n\nThis is Complet Order List.\n\n\
    \rTotal for pay:{sum(total):>79.1f}{list_of_menu[i][4]:>7s}')
