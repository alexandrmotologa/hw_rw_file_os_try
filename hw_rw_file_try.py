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


# sortarea listei menu
def menu_sort():
    for j in range(len(list_of_menu)):
            for i in range(len(list_of_menu) - 1):
                if list_of_menu[i][0] > list_of_menu[i + 1][0]:
                    temp = list_of_menu[i]
                    list_of_menu[i] = list_of_menu[i + 1]
                    list_of_menu[i + 1] = temp


# sortarea listei order
def order_sort():
    for j in range(len(list_of_order)):
            for i in range(len(list_of_order) - 1):
                if list_of_order[i][0] > list_of_order[i + 1][0]:
                    temp = list_of_order[i]
                    list_of_order[i] = list_of_order[i + 1]
                    list_of_order[i + 1] = temp


menu_sort()
order_sort()

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
    \t\t\t\t\t\t\t\tTotal for pay:{sum(total):>15.1f}{list_of_menu[i][4]:>7s}')
