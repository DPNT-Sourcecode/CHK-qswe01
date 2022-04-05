

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = list(skus)
    items_set = set(items)
    prices = {"A": 50, 
    "B": 30, 
    "C": 20, 
    "D": 15, 
    "E": 40, 
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
    }
    special_offer = "ABF"

    def discountA(basket):
        q5A, rest5 = divmod(amount, 5)
        q3A, rest3 = divmod(rest5, 3)
        subtotal = (q5A*200 + q3A*130 + rest3*prices.get(item))
        return subtotal

    def discountB(basket):
        qE, _ = divmod(basket.get("E", 0), 2)
        newAmountB = max(0, basket.get(item) - qE)
        qB, restB = divmod(newAmountB, 2)
        subtotal = qB*45 + restB*prices.get(item)
        return subtotal
    discounts = {"A": discountA, "B": discountB}



    # fill basket from string
    basket = {}
    for item in items_set:
        if item not in prices.keys():
            return -1

        basket[item] = items.count(item)

    # sum up cost
    total = 0
    for item, amount in basket.items():
        if item not in special_offer:
            total += amount * prices.get(item)
        else:
            if item == "A":
                #q5A, rest5 = divmod(amount, 5)
                #q3A, rest3 = divmod(rest5, 3)
                #total += (q5A*200 + q3A*130 + rest3*prices.get(item))
                discount = discounts.get("A")
                total += discount(basket)
            elif item == "B":       
                #qE, _ = divmod(basket.get("E", 0), 2)
                #newAmountB = max(0, basket.get(item) - qE)

                #qB, restB = divmod(newAmountB, 2)
                discount = discounts.get("B")
                total += discount(basket)
            elif item == "F":
                qF, restF = divmod(basket.get(item), 3)
                newAmountB = basket.get(item) - qF

                total += newAmountB * prices.get(item)
                
    return total

print(checkout("AAAA"))
print(checkout("BBBB"))
#print(checkout("C"))
#print(checkout("D"))
#print(checkout("ABCD"))
#print(checkout("ABCDEE"))
#print(checkout("AAAAAABCD"))
print(checkout("EEEEBB"))   #160
#print(checkout("BEBEEE"))   #160
print(checkout("ABCDEABCDE"))   #280
#print(checkout("EEB")) # 80
#print(checkout("EEEB")) # 120
print(checkout("FF"))
print(checkout("FFF"))
print(checkout("FFFFF"))
print(checkout("FFFFFF"))

        

        


"""
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+
 """

