#Suppose the cover price of a book is $24.95,
#but bookstores get a 40% discount. Shipping
#costs $3 for the first copy and 75 cents for
#each additional copy. What is the total
#wholesale cost for 60 copies?

price=float(input("please input the price : "))
discount=int(input("please input the discount amount :"))/100
ShippingFirst=3
ShippingAddit=0.75
totalCopies=60

bookcost=totalCopies*price*(1-discount)
shippingcost=ShippingFirst+ShippingAddit*(totalCopies-1)

totalCost=bookcost+shippingcost
print(totalCost)



