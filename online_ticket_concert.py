import tkinter as tk

import mysql.connector

# Connect MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="online_ticket_concert"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

def calculate_total():
    # Get the selected ticket price from the type_ticket_var
    selected_ticket = type_ticket_var.get()
    ticket_prices = {"Tier A": 400, "Tier B": 500, "Tier C": 600}
    ticket_price = ticket_prices.get(selected_ticket, 0)
    

    # Get the quantity
    quantity = int(quantity_box.get())

    merchandise_choice = check_var_yes.get()

    # Calculate the total price including the ticket and merchandise
    if merchandise_choice == 1:
        merchandise_price = 50
        total_price = ((ticket_price * quantity) + merchandise_price)
        

    else:
        total_price = (ticket_price * quantity)


    # Display the total price
    output_label.config(text=f"Total Price: RM {total_price}")

    # To insert data into database, modify the following lines:
    sql = "INSERT INTO customer_ticket_order (Name, Email, Phone, Quantity, Ticket_Type, Merchandise, Total_Price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name_entry.get(), email_entry.get(), no_phone_entry.get(), quantity_box.get(), type_ticket_var.get(), "Yes" if merchandise_choice == 1 else "No", total_price)
    mycursor.execute(sql, val)
    mydb.commit()

# Create a window
root = tk.Tk()
root.geometry("600x620")
root.title("Online Ticket Concert Order")
root.configure(background='#798777')


# Add a label
Label = tk.Label(root, text = "ATEEZ Online Ticket Concert", font = ('Century', 15), bg='#E4DCCF')
Label.pack(padx=20, pady=10)



# Prices List by using textbox
tier_ticket_type = tk.Text(root, height=10, width=20, font=('New York', 12), bg='#E4DCCF')
tier_ticket_type.pack(pady=10)

# The prices of ticket
tier_ticket_type.insert(tk.END, "Prices of Ticket:\n\n")
tier_ticket_type.insert(tk.END, "Tier A: RM400\n\n")
tier_ticket_type.insert(tk.END, "Tier B: RM500\n\n")
tier_ticket_type.insert(tk.END, "Tier C: RM600\n\n")
tier_ticket_type.configure(state='disabled')


frame = tk.Frame(root, bg='#E4DCCF')
frame.pack()

# Customer Order Frame
customer_order_frame =tk.LabelFrame(frame, text="Customer Order", bg='#E4DCCF')
customer_order_frame.grid(row= 1, column=0, padx=5, pady=5)

# Customer Label
name_label = tk.Label(customer_order_frame, text="Name", bg='#E4DCCF')
name_label.grid(row=0, column=0, padx=5, pady=5)
email_label = tk.Label(customer_order_frame, text="Email", bg='#E4DCCF')
email_label.grid(row=0, column=1, padx=5, pady=5)
no_phone_label = tk.Label(customer_order_frame, text="No Phone", bg='#E4DCCF')
no_phone_label.grid(row=0, column=2, padx=5, pady=5)


# Customer Enter
name_entry = tk.Entry(customer_order_frame, bg='#F8EDE3')
name_entry.grid(row=1, column=0, padx=5, pady=5)
email_entry = tk.Entry(customer_order_frame, bg='#F8EDE3')
email_entry.grid(row=1, column=1, padx=5, pady=5)
no_phone_entry = tk.Entry(customer_order_frame, bg='#F8EDE3')
no_phone_entry.grid(row=1, column=2, padx=5, pady=5)


# Ticket Information Frame
ticket_order_frame =tk.LabelFrame(frame, text="Ticket Order Information", bg='#E4DCCF')
ticket_order_frame.grid(row= 2, column=0, padx=10, pady=10)

# Quantity of ticket
quantity_box_label = tk.Label(ticket_order_frame, text="Quantity", bg='#E4DCCF')
quantity_box_label.grid(row=2, column=1, padx=10, pady=10)
quantity_box = tk.Spinbox(ticket_order_frame, from_= 0, to = 10, bg='#F8EDE3') 
quantity_box.grid(row=2, column= 2, padx=10, pady=10)

# Dropdown of type ticket
type_ticket_var = tk.StringVar(ticket_order_frame)
type_ticket_var.set("Select Your Ticket") 
ticket_tier_dropdown = tk.OptionMenu(ticket_order_frame, type_ticket_var, "Tier A", "Tier B", "Tier C")
ticket_tier_dropdown.grid(row=2, column=3, pady=10)
ticket_tier_dropdown.config(bg='#E4DCCF') 
ticket_tier_dropdown["menu"].config(bg='#E4DCCF')


# Merchandise 
merchandise_frame =tk.LabelFrame(frame, text='Merchandise', bg='#E4DCCF')
merchandise_frame.grid(row= 3, column=0, padx=10, pady=10)
check_var_yes = tk.IntVar()
check_button_yes = tk.Checkbutton(merchandise_frame, text="Yes", variable=check_var_yes, bg='#E4DCCF')
check_button_yes.grid(row=3, column=1, padx=10, pady=10)
check_var_no = tk.IntVar()
check_button_no = tk.Checkbutton(merchandise_frame, text="No", variable=check_var_no, bg='#E4DCCF')
check_button_no.grid(row=3, column=2, padx=10, pady=10)


# Submit and Calculate Button
calculate_save_button = tk.Button(text = "Calculate & Submit", width=15, command=calculate_total, bg='#E4DCCF')
calculate_save_button.pack(padx= 5, pady=5, side="top")

# Output
label = tk.Label(root, text='Price Package', bg='#798777')
label.pack(padx=5, pady=5)
output_label = tk.Label(root, text="", bg='#798777')
output_label.pack()


# Run the application
root.mainloop()