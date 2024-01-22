costprice=int(input("Enter Cost price of the product:"))
sellingprice=int(input("Enter Selling Price of the product:"))

if sellingprice>costprice:
    profit=sellingprice-costprice
    print(profit," profit")
elif costprice>sellingprice:
    loss=costprice-sellingprice
    print(loss," loss")
else:
    print("No profit no loss")