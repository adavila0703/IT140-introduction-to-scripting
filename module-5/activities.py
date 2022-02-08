# def number_of_pennies(dollars, *args):
#     pennies = 0

#     for p in args:
#         pennies += p

#     return dollars * 100 + pennies


# test = number_of_pennies(5, 10, 100, 10)

# print(test)


def split_check(bill, people, *args):
    total_bill = bill
    tax = 0.09
    tip = 0.15

    if len(args) == 0:
        total_bill += (bill * tax) + (bill * tip)
        return total_bill / people
    if len(args) >= 1:
        tax = bill * args[0]
        total_bill += tax
    if len(args) >= 2:
        tip = bill * args[1]
        total_bill += tip

    return total_bill / people


bill = float(input())
people = int(input())

# Cost per diner at the default tax and tip percentages
print('Cost per diner:', split_check(bill, people))

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

# Cost per diner at different tax and tip percentages
print('Cost per diner:', split_check(
    bill, people, new_tax_percentage, new_tip_percentage))
