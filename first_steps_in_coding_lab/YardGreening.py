square_meter = float(input())

final_price = square_meter * 7.61
discount_price = final_price * 0.18
final_price_wo_vat = final_price - discount_price

print(f"The final price is: {final_price_wo_vat} lv.")
print(f"The discount is: {discount_price} lv.")