(product)= input("Product Name:")
(price)= input("Price per unit:")
(qty)= input("qty of:")
amount = float(price)*int(qty)
vat= float(amount/100*20)
bill= float(amount) + float(vat)
print("Product:", product)
print("Amount is:", amount)
print("VAT is:", int(vat))
print("Total cost:£", float(bill))
