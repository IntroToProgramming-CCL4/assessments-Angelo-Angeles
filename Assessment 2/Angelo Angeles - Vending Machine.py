import tkinter as tk
from collections import Counter

# I WAS TOO AMBITIOUS IT TOOK SO MUCH TIME THAT I HAVE NONE LEFT AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH HELP!!! PS: I give up making this fancy. Jan 9th

# Variable Library
Money = 50 # Reminder Self: Add a functionality where the user inputs own money. or has options
PLYRInput = ["‎","‎"] # God figuring this out was a doozy, note to self that you shouldn't touch this and just leave it as is before everything breaks
Cart = []
Category = ""
Display_Item = ""
total_price = 0
Display_Menu = """
A1 Foods:\n
    A1: Lay's Classic - Price: $5.50\n
    A2: Lay's Ketchup - Price: $5.50\n
    A3: Lay's Salt and Vinegar - Price: $5.50\n
    B1: Doritos Nacho Cheese - Price: $7.00\n
    B2: Doritos Sweet Chili - Price: $7.00\n
    B3: Nova Multigrain Chips - Price: $6.50\n
    C1: Cheetos Crunchy - Price: $6.00\n
    C2: Cheetos Flamin' Hot - Price: $6.00\n
    C3: Bugles - Price: $3.50\n
A2 Drinks:\n
    A1: Coca Cola - Price: $3.50\n
    A2: Pepsi - Price: $3.50\n
    A3: Mountain Dew - Price: $3.50\n
    B1: Sprite - Price: $3.50\n
    B2: Fanta - Price: $3.50\n
    B3: Lipton Iced Tea - Price: $4.50\n
    C1: Lipton Peace Iced Tea - Price: $4.50\n
    C2: Strawberry Milk - Price: $2.50\n
    C3: Chocolate Milk - Price: $2.50\n"""
# My Menu, Yes i know it is basic Sir. But cmon idk what to put in here! Also it took me like 30 minutes to figure out what i should even put in here
Menu = {
    "A1":{"Foods":{
        "A1":{"Product":"Lay's Classic", "Price":5.50},
        "A2":{"Product":"Lay's Ketchup", "Price":5.50},
        "A3":{"Product":"Lay's Salt and Vinegar", "Price":5.50},
        "B1":{"Product":"Doritos Nacho Cheese", "Price":7.00},
        "B2":{"Product":"Doritos Sweet Chili", "Price":7.00},
        "B3":{"Product":"Nova Multigrain Chips", "Price":6.50},
        "C1":{"Product":"Cheetos Crunchy", "Price":6.00},
        "C2":{"Product":"Cheetos Flamin' Hot", "Price":6.00},
        "C3":{"Product":"Bugles", "Price":3.50},
    }},
    "A2":{"Drinks":{
        "A1":{"Product":"Coca Cola", "Price":3.50},
        "A2":{"Product":"Pepsi", "Price":3.50},
        "A3":{"Product":"Mountain Dew", "Price":3.50},
        "B1":{"Product":"Sprite", "Price":3.50},
        "B2":{"Product":"Fanta", "Price":3.50},
        "B3":{"Product":"Lipton Iced Tea", "Price":4.50},
        "C1":{"Product":"Lipton Peace Iced Tea", "Price":4.50},
        "C2":{"Product":"Strawberry Milk", "Price":2.50},
        "C3":{"Product":"Chocolate Milk", "Price":2.50},
    }}
}

# Windows
# Creating Window
Vending = tk.Tk()
Console = tk.Tk()

# Window Settings
Vending.geometry("900x800+550+10")
Vending.title("Vending Machine")
Vending['bg'] = "#121212"

Console.geometry("250x500+100+10")
Console.title("Console")
Console['bg'] = "#121212"

# Objects
# Vending Machine Window Objects
Text_Vending = tk.Label(Vending, text="Vending Machine", font=('Helvetica', '24'),fg="#ffffff",bg="#121212")
Text_Vending.pack(pady=10)

# OH MY GOD I AM SO DONE WITH THIS TEXTBOX THING IT TAKES UP SO MANY LINES BUT IDK HOW TO MAKE IT BETTERRRRRRRRRRR
Display = tk.Text(Vending, font=('Helvetica', '14'), bg="#121212", fg="#ffffff")
Display.insert(tk.END,
f"""
INSTRUCTIONS!
1) USE YOUR CONSOLE TO INPUT CODES AND SELECT WHAT YOU NEED!
2) TO SELECT BETWEEN FOODS OR DRINK INPUT A1 FOR FOR FOOD AND A2 FOR DRINK AND THEN SELECT THE 'CATEGORY' BUTTON!
3) YOU CAN SCROLL DOWN TO SEE MORE OPTIONS!
4) YOU HAVE 50$ TO DO WHATEVER!
5) YOU CAN ALWAYS RESET WITH THE RESET BUTTON!\n\n
{Display_Menu}""")
Display.config(state=tk.DISABLED)
Display.pack(pady=10, padx=10)

# Console Window Objects
Text_Console = tk.Label(Console, text="Console",fg="#ffffff", bg="#121212", font=('Helvetica', '14'))
Text_Console.pack(padx=10, pady=10)

PLYR = tk.Label(Console, text=PLYRInput, font=('Helvetica', '14'), bg="#121212", fg="#ffffff", border=10)
PLYR.pack(padx=10, pady=20)

# I am dying. Jan 8th, 2AM

# Function Library
def cmdButton_A():
    global PLYR
    PLYRInput[0]="A"
    PLYR["text"]=PLYRInput
def cmdButton_B():
    global PLYR
    PLYRInput[0]="B"
    PLYR["text"]=PLYRInput  
def cmdButton_C():
    global PLYR
    PLYRInput[0]="C"
    PLYR["text"]=PLYRInput 
def cmdButton_1():
    global PLYR
    PLYRInput[1]="1"
    PLYR["text"]=PLYRInput  
def cmdButton_2():
    global PLYR
    PLYRInput[1]="2"
    PLYR["text"]=PLYRInput   
def cmdButton_3():
    global PLYR
    PLYRInput[1]="3"
    PLYR["text"]=PLYRInput
def cmdButton_reset():
    global PLYR, PLYRInput, Money, total_price, Cart, Display_Item, Display
    PLYRInput = ["‎","‎"]
    Money = 50
    Cart = []
    Display_Item = ""
    total_price = 0
    Display = tk.Text(Vending, font=('Helvetica', '14'), bg="#121212", fg="#ffffff")
    # oh my god i need to paste it again here.......
    Display.config(state=tk.NORMAL)
    Display.delete("1.0", tk.END)
    Display.insert(tk.END,
    f"""
    INSTRUCTIONS!
    1) USE YOUR CONSOLE TO INPUT CODES AND SELECT WHAT YOU NEED!
    2) TO SELECT BETWEEN FOODS OR DRINK INPUT A1 FOR FOR FOOD AND A2 FOR DRINK AND THEN SELECT THE 'CATEGORY' BUTTON!
    3) YOU CAN SCROLL DOWN TO SEE MORE OPTIONS, THE MENU IS ALWAYS THERE!!
    4) YOU HAVE 50$ TO DO WHATEVER!
    5) YOU CAN ALWAYS RESET WITH THE RESET BUTTON!

    {Display_Menu}""")
    Display.config(state=tk.DISABLED)
    # my line count.... ;-;
    PLYR["text"]=PLYRInput  
def cmdButton_enter():
    global PLYRInput, Cart, Category, Display, Money
    Code = "".join(PLYRInput) 
    if Category in Menu:
        category_data = Menu[Category]
        if "Foods" in category_data and Code in category_data["Foods"]:
            selected_item = category_data["Foods"][Code]
        elif "Drinks" in category_data and Code in category_data["Drinks"]:
            selected_item = category_data["Drinks"][Code]
        else:
            selected_item = None
        if selected_item:
            # This will just check.... if there is enough money to make the purchase
            if Money >= selected_item['Price']:
                # And this will just deduct the price from the Money variable
                Money -= selected_item['Price']
                Cart.append(selected_item)
                # HOW MANY OF THESE DO I HAVE TO DOOOOOOOO
                Display.config(state=tk.NORMAL)
                Display.delete("1.0", tk.END)
                Display.insert(tk.END, f"Product: {selected_item['Product']} - Price: ${selected_item['Price']:.2f}\n")
                Display.insert(tk.END, f"Remaining Money: ${Money:.2f}\n")
                Display.insert(tk.END, f"\n\n===MENU===\n{Display_Menu}")
                Display.config(state=tk.DISABLED)
            else:
                Display.config(state=tk.NORMAL)
                Display.delete("1.0", tk.END)
                Display.insert(tk.END, "Insufficient funds. Cannot make the purchase.\n")
                Display.insert(tk.END, f"\n\n===MENU===\n{Display_Menu}")
                Display.config(state=tk.DISABLED)
        else:
            Display.config(state=tk.NORMAL)
            Display.delete("1.0", tk.END)
            Display.insert(tk.END, "Invalid Code\n")
            Display.insert(tk.END, f"\n\n===MENU===\n{Display_Menu}")
            Display.config(state=tk.DISABLED)
    PLYRInput = ["‎", "‎"]
    PLYR["text"] = PLYRInput
def cmdButton_CAT(): # TOTAL NUMBER OF RETRIES TRYING TO MAKE THIS WORK: 10000000. nah tbh i lost count
    global PLYRInput, Category, Display

    if len(PLYRInput) == 2 and PLYRInput[0] == "A" and PLYRInput[1] in ["1", "2"]:
        Category = "".join(PLYRInput)

        category_text = "FOODS" if PLYRInput[1] == "1" else "DRINKS"
        Display.config(state=tk.NORMAL)
        Display.delete("1.0", tk.END)
        Display.insert(tk.END, f"Selected Category: {category_text}!\n")
        Display.insert(tk.END, f"\n\n===MENU===\n{Display_Menu}")
        Display.config(state=tk.DISABLED)
    else:
        Display.config(state=tk.NORMAL)
        Display.delete("1.0", tk.END)
        Display.insert(tk.END, "Invalid Code\n")
        Display.insert(tk.END, f"\n\n===MENU===\n{Display_Menu}")
        Display.config(state=tk.DISABLED)
        print("Invalid Code")
def cmdButton_Cart(): # THIS IS THE WORSSTTTTTTTTT
    # You know what imma make this the receipt thing. Jan 10th
    global Cart, Display, total_price
    cart_counts = Counter(tuple(item.items()) for item in Cart)
    cart_details = ""
    for item, count in cart_counts.items():
        product = item[0][1]
        price = item[1][1]
        total_price += price * count
        # Look at me using fancy formatting like {:.2f} keke... I need sleep
        if count > 1:
            cart_details += "{} x{} - Price: ${:.2f}\n".format(product, count, price * count)
        else:
            cart_details += "{} - Price: ${:.2f}\n".format(product, price)
    #Ayyyy finally got this total price thing to work (Jan 9th, 3AM... HELP MEEE)
    cart_details += "\nTotal Price: ${:.2f}".format(total_price)
    Display.config(state=tk.NORMAL)
    Display.delete("1.0", tk.END)
    Display.insert(tk.END, cart_details)
    Display.config(state=tk.DISABLED)
# Button Making
# Button frame
Console_Buttons = tk.Frame(Console)
Console_Buttons.config(height=400, width=230, bg="#121212")

# Buttons (THIS IS TOO INEFFICIENT BUT I AM OUT OF TIME)
Button_A = tk.Button(Console_Buttons, text="A", font=("Helvetica", 18), bg="#121212", fg="#ffffff", command=cmdButton_A,height=2, width=5)
Button_A.grid(row=0, column=0, sticky="news")
Button_B = tk.Button(Console_Buttons, text="B", font=("Helvetica", 18), bg="#121212", fg="#ffffff", command=cmdButton_B,height=2, width=5)
Button_B.grid(row=0, column=1, sticky="news")
Button_C = tk.Button(Console_Buttons, text="C", font=("Helvetica", 18), bg="#121212", fg="#ffffff", command=cmdButton_C,height=2, width=5)
Button_C.grid(row=0, column=2, sticky="news")
Button_1 = tk.Button(Console_Buttons, text="1", font=("Helvetica", 18), bg="#121212", fg="#ffffff", command=cmdButton_1,height=2, width=5)
Button_1.grid(row=1, column=0, sticky="news")
Button_2 = tk.Button(Console_Buttons, text="2", font=("Helvetica", 18), bg="#121212", fg="#ffffff", command=cmdButton_2,height=2, width=5)
Button_2.grid(row=1, column=1, sticky="news")
Button_3 = tk.Button(Console_Buttons, text="3", font=("Helvetica", 18), bg="#121212", fg="#ffffff", command=cmdButton_3,height=2, width=5)
Button_3.grid(row=1, column=2, sticky="news")
Button_Clear = tk.Button(Console_Buttons, text="RESET", font=("Helvetica", 10), bg="#121212", fg="#ffffff", command=cmdButton_reset,height=5, width=5)
Button_Clear.grid(row=3, column=2, sticky="news")
Button_Clear = tk.Button(Console_Buttons, text="ADD", font=("Helvetica", 10), bg="#121212", fg="#ffffff", command=cmdButton_enter,height=5, width=5)
Button_Clear.grid(row=3, column=0, sticky="news")
Button_CAT = tk.Button(Console_Buttons,text="CATEGORY",font=("Helvetica", 10), bg="#121212", fg="#ffffff", command=cmdButton_CAT,height=5, width=5)
Button_CAT.grid(row=3, column=1, sticky="news")
Button_Cart = tk.Button(Console_Buttons,text="RECEIPT",font=("Helvetica", 10), bg="#121212", fg="#ffffff", command=cmdButton_Cart,height=5, width=5)
Button_Cart.grid(row=4, column=1, sticky="news")

# Wow thats alot of buttons.

Console_Buttons.pack(pady=10)


# Ending
Vending.mainloop()
Console.mainloop()