

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # modify input to take care of group items
    group = ""
    for char in "ZSTYX":
        group += skus.count(char) * char
        skus = skus.replace(char, "")

    groupDiscountItems, _ = divmod(len(group), 3)
    leftOver = group[groupDiscountItems*3:]
    skus += leftOver
    
    
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
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
    }

    # discount functions
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

    def discountF(basket):
        qF, restF = divmod(basket.get(item), 3)
        newAmountB = basket.get(item) - qF
        subtotal = newAmountB * prices.get(item)
        return subtotal

    def discountH(basket):
        q10H, rest10 = divmod(amount, 10)
        q5H, rest5 = divmod(rest10, 5)
        subtotal = (q10H*80 + q5H*45 + rest5*prices.get(item))
        return subtotal

    def discountK(basket):
        qK, restK = divmod(basket.get(item), 2)
        subtotal = qK *120 + restK * prices.get(item)
        return subtotal
 
    def discountP(basket):
        qK, restK = divmod(basket.get(item), 5)
        subtotal = qK *200 + restK * prices.get(item)
        return subtotal
        
    def discountQ(basket):
        qR, _ = divmod(basket.get("R", 0), 3)
        newAmountQ = max(0, basket.get(item) - qR)
        qQ, restQ = divmod(newAmountQ, 3)
        subtotal = qQ*80 + restQ * prices.get(item)
        return subtotal   
        
    def discountV(basket):
        q3H, rest3 = divmod(amount, 3)
        q2H, rest2 = divmod(rest3, 2)
        subtotal = (q3H*130 + q2H*90 + rest2*prices.get(item))
        return subtotal
        
    def discountM(basket):
        qN, _ = divmod(basket.get("N", 0), 3)
        newAmountN = max(0, basket.get(item) - qN)
        subtotal = newAmountN * prices.get(item)
        return subtotal

    def discountU(basket):
        qU, _ = divmod(basket.get(item), 4)
        newAmountU = max(0, basket.get(item) - qU)
        subtotal = newAmountU * prices.get(item)
        return subtotal

    discounts = {"A": discountA, "B": discountB, "F": discountF, "H": discountH, "K": discountK, 
    "P": discountP, "Q": discountQ, "V": discountV, "M": discountM, "Q":discountQ, "U":discountU}


    # fill basket from string
    basket = {}
    for item in items_set:
        if item not in prices.keys():
            return -1

        basket[item] = items.count(item)

    # sum up cost
    total = 0
    for item, amount in basket.items():
        if item not in discounts.keys():
            total += amount * prices.get(item)
        else:
            discount = discounts.get(item)
            total += discount(basket)

    # add group discount
    total += groupDiscountItems * 45

    return total

#print(checkout("AAAA"))
#print(checkout("BBBB"))
##print(checkout("C"))
##print(checkout("D"))
##print(checkout("ABCD"))
##print(checkout("ABCDEE"))
##print(checkout("AAAAAABCD"))
#print(checkout("EEEEBB"))   #160
##print(checkout("BEBEEE"))   #160
#print(checkout("ABCDEABCDE"))   #280
##print(checkout("EEB")) # 80
##print(checkout("EEEB")) # 120
##print(checkout("FF"))
##print(checkout("FFF"))
##print(checkout("FFFFF"))
##print(checkout("FFFFFF"))
#print(checkout("HHHHH"))
#print(checkout("HHHHHHHHHHH"))
#print(checkout("HHHH"))
#print(checkout("KKK"))
#print(checkout("V"))
#print(checkout("VV"))
#print(checkout("VVV"))
#print(checkout("NNNMM"))
#print(checkout("RRRQ"))
#print(checkout("UUUUUU"))
#print(checkout("UUU")) # 120
#print(checkout("QQQ"))  #80
#print(checkout("QQQQ")) #110
#print(checkout("XYZSTSS"))
#print(checkout("K"))    # 70
#print(checkout("ABCDEFGHIJKLMNOPQRSTUVW"))  # 795
#print(checkout("KK"))    # 120
#print(checkout("KKK"))    # 190
#print(checkout("KKKK"))    # 240



"""
+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+
 """