#if statement
# age = int(input("Enter your age: "))
# if age >= 18 and age <= 45:
#     print("You are a young blood") 


#if-else statement
# price = int (input("Enter the product price: "))
# if price > 1000:
#     print("The discounted price is: ", 0.8*price)
# else:
#     print("The discounted price is: ", 0.7*price)


#if-elif-else
# price = int(input("Enter the product price: "))
# if price>3000:
#     print("The discounted price is: {}".format(0.8*price))
# elif price > 2000 and price <= 3000:
#     print("The discounted price is: {}".format(0.7*price))
# elif price >= 1000 and price <= 2000:
#     print("The discounted price is {}".format(0.6*price))
# else:
#     print("You have to pay the full price")


#nested if
# price = int(input("Enter the product price: "))
# if price>3000:
#     print("The discounted price is: {}".format(int(0.8*price)))
# elif price > 2000 and price <= 3000:
#     print("The discounted price is: {}".format(int(0.7*price)))
#     if price == 2999:
#         print("You won an additional gift")
# elif price >= 1000 and price <= 2000:
#     print("The discounted price is {}".format(int(0.6*price)))
# else:
#     print("You have to pay the full price")