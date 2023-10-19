numb_ticket = int(input("Укажите количество билетов: "))
price = 0
ticket_age ={}
while numb_ticket > 0:
    age = int(input("Введите возраст: "))
    ticket_age[numb_ticket] = age
    numb_ticket = numb_ticket -1
ticket_age_items = ticket_age.items()
for numb, age in ticket_age_items:
    if 18 <= age <= 25:
        price = price + 990
    elif age > 25:
        price = price + 1390
    elif age < 18:
        price = price
if numb_ticket > 3:
    price = price - (price * 0.1 )
price = str(price)
print("Сумма к оплате: ", price )
