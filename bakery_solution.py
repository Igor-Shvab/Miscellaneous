"""
Data in lookup_table has following format:
{product_code: [(price, batch),(price, batch)...], 
product_code: [(price, batch),(price, batch)...],
...}
"""
#prod_names = [('Vegimite Scroll','VS5'), ('Blueberry Muffin','MB11'), ('Croissant','CF')]
#prod_lookup = {'VS5':[(8.99,5), (6.99,3)],'MB11':[(24.65,8), (16.95,5), (9.95,2)],'CF': [(16.99,9), (9.95,5), (5.95,3)]}

from lookup_table import *


"""
Following function calculates minimal quantity of product in batches and returns order breakdown in following format:
{price: quantity, price: quantity, ...}
"""
def coins_given(amount, coins):
    answer = {}
    answer_value = {}
    for coin_name, coin_value in coins:
        if amount >= coin_value:
            number_coin, amount = divmod(amount, coin_value)
            answer[coin_name] = number_coin
            answer_value[coin_name] = coin_value

    sum_ = 0
    for k in answer.keys():
    	sum_ += k*answer[k]

    return [answer, sum_, answer_value]


if __name__ == '__main__':

    print('Hi, in our bakery you can purchase following products:\n')
    for i in dict(prod_names).keys():
    	print(i.ljust(30) + 'code = ' + dict(prod_names)[i])

    print('\nPlease enter product code and product quantity. \nWhen you are done with your orders press spacebar.')

    cart = {}   # Output in this format: {'CF': 10, 'VS5': 11}
    coins = []  # Output in this format: [('CF', 10), ('VS5', 11)]

    # User interaction
    # FOLLOWING INPUT FORMAT REQUIRED:   product_code,rpoduct_quantity
    # Can handle wrong product_code
    # Can handle noninteger product_quantity
    # Adds up product_quantities for product_codes that are repeated
    # USER CAN EXXIT BY PRESSING ENTER
    while True:
         user_input = raw_input("Enter product code and quanyity separated by comma: ")
         if (user_input.split(',')[0] in dict(prod_names).values()) and (user_input.split(',')[1].isdigit()):
            if user_input.split(',')[0] in cart.keys():
            	cart[user_input.split(',')[0]] += int(round(float(user_input.split(',')[1])))
            else:
            	cart[user_input.split(',')[0]] = int(round(float(user_input.split(',')[1])))
         if user_input == "":
         	break
         elif user_input.split(',')[0] not in dict(prod_names).values():
         	print('Incorrect product code. Retype your order or press Enter to finish:')
         elif not user_input.split(',')[1].isdigit() :
         	print('Incorrect product quantity. Type integer or press Enter to finish:')

    # Coverting dictionary to list of tuples
    for i in cart.items():
    	coins.append(i)

    # Results
    print('')
    for i,j in coins:
        print('%d %s $%f' %(j, i, coins_given(j, prod_lookup[i])[1]))
        for k in coins_given(j, prod_lookup[i])[0]:
            print('\t' + str(coins_given(j, prod_lookup[i])[0][k]) + ' x ' + str(coins_given(j, prod_lookup[i])[2][k]) + ' $%.2f' %k)

