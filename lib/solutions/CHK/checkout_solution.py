

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = list(skus)
    items_set = set(items)
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
    special_offer = "ABF"

    basket = {}
    for item in items_set:
        if item not in prices.keys():
            return -1

        basket[item] = items.count(item)

    total = 0

    #if basket.get("B") and basket.get("E"):
    #    q, rest = divmod(basket.get("E"), 2)
    #    if basket.get("B") >= q:
    #        basket["B"] = basket.get("B") - q
    #    else:
    #        basket["B"] = 0
    #print(basket)

    for item, amount in basket.items():
        if item not in special_offer:
            total += amount * prices.get(item)
        else:
            if item == "A":
                q5A, rest5 = divmod(amount, 5)
                q3A, rest3 = divmod(rest5, 3)
                total += (q5A*200 + q3A*130 + rest3*prices.get(item))
            elif item == "B":       
                qE, _ = divmod(basket.get("E", 0), 2)
                newAmountB = max(0, basket.get(item) - qE)

                qB, restB = divmod(newAmountB, 2)
                total += qB*45 + restB*prices.get(item)
            elif item == "F":
                qF, restF = divmod(basket.get(item), 3)
                newAmountB = basket.get(item) - qF

                total += newAmountB * prices.get(item)
                
    return total

#print(checkout("AAAA"))
#print(checkout("BBBB"))
#print(checkout("C"))
#print(checkout("D"))
#print(checkout("ABCD"))
#print(checkout("ABCDEE"))
#print(checkout("AAAAAABCD"))
#print(checkout("EEEEBB"))   #160
#print(checkout("BEBEEE"))   #160
#print(checkout("ABCDEABCDE"))   #280
#print(checkout("EEB")) # 80
#print(checkout("EEEB")) # 120
print(checkout("FF"))
print(checkout("FFF"))
print(checkout("FFFFF"))
print(checkout("FFFFFF"))

        

        


"""
A new item has arrived. Item F.
Our marketing team wants to try rewording the offer to see if it affects consumption
Instead of multi-pricing this item they want to say "buy 2Fs and get another F free"
The offer requires you to have 3 Fs in the basket.

Our price table and offers: 
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
+------+-------+------------------------+
 """