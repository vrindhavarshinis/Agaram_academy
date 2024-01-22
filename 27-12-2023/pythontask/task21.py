unit=int(input("Enter Your Electricity Units:"))
if unit<=50:
    billamount=(unit*0.50)
    print("Billamount:",(billamount)+(billamount*20/100))
elif unit<=150:
    billamount=(50*0.50)+(unit-50)*0.75
    print("Billamount:",(billamount)+(billamount*20/100))
elif unit<=250:
    billamount=(50*0.50)+(100*0.75)+((unit-150)*1.20)
    print("Billamount:",(billamount)+(billamount*20/100))
elif unit>250:
    billamount=(50*0.50)+(100*0.75)+(100*1.20)((unit-250)*1.50)
    print("Billamount:",(billamount)+(billamount*20/100))
