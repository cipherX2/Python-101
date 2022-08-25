import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(f"                                    Time:  {current_time}           ")


stock_name = input("Enter Stockname: ").capitalize()

buying_price = float(input("Enter buying price: "))
quantity = float(input("Enter quantity: "))
stop_loss_amount = float(input("Enter stoplots value: "))

total_amount = buying_price * quantity
stop_loss_value = round(stop_loss_amount / total_amount, 4)
stop_loss_percent = round(stop_loss_value * 100, 3)
stop_loss_point = round((stop_loss_percent * buying_price) / 100, 4)

stop_loss = round(buying_price - stop_loss_point, 3)

print("                                       Stocks info\n\n")
print(f"Total amount(TM) : {total_amount}")
print(f"Stop loss value(SLV): {stop_loss_value}")
print(f"Stop loss percent(SL%): {stop_loss_percent}")
print(f"Stop loss point(SLP): {stop_loss_point}")
print(f"Stop Loss(SL): {stop_loss}")
