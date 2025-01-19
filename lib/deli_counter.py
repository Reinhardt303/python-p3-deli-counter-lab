def line(customers):
    if len(customers) == 0:
        print("The line is currently empty.") 
    elif len(customers) > 0: 
        line_list = [(f"{(customers.index(customer)) + 1}. {customer}") for customer in customers]
        print(f"The line is currently: {' '.join(line_list)}")


def take_a_number(customers, new_customer):
    if len(customers) == 0:
        message = (f"Welcome, {new_customer}. You are number 1 in line.")
        print(message)
        customers.append(new_customer)
    elif len(customers) > 0:
        customers.append(new_customer)
        message = (f"Welcome, {new_customer}. You are number {customers.index(new_customer) + 1} in line.")
        print(message)


def now_serving(customers):
    if len(customers) == 0:
        print("There is nobody waiting to be served!")
    elif len(customers) > 0:
        print(f"Currently serving {customers[0]}.")
        del customers[0]
