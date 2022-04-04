

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = list(skus)
    items_set = set(items)
    stock = "ABCDE"
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    special_offer = "AB"

    total = 0

    basket = {}
    for item in items_set:
        if item not in stock:
            return -1

        basket[item] = items.count(item)

    return basket

    #for item in items_set:
    #    if item not in stock:
    #        return -1
    #    
    #    amount = items.count(item)
    #    if item not in special_offer:
    #        total += (amount * prices.get(item))
    #    else:
    #        if item == "A":
    #            q5A, rest5 = divmod(amount, 5)
    #            q3A, rest3 = divmod(rest5, 3)
    #            total += (q5A*200 + q3A*130 + rest3*prices.get(item))
    #        elif item == "B":
    #            q, rest = divmod(amount, 2)
    #            total += (q*45 + rest*prices.get(item))
    #        elif item == "E":
#
    return total


print(checkout("AAAA"))
print(checkout("BBBB"))
print(checkout("C"))
print(checkout("D"))
print(checkout("ABCD"))
print(checkout("ABCDE"))
print(checkout("AAAAAABCD"))


        

        


"""
Our price table and offers: 
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+


Notes: 
 - The policy of the supermarket is to always favor the customer when applying special offers.
 - All the offers are well balanced so that they can be safely combined.
 - For any illegal input return -1

In order to complete the round you need to implement the following method:
     checkout(String) -> Integer

Where:
 - param[0] = a String containing the SKUs of all the products in the basket
 - @return = an Integer representing the total checkout value of the items 
 """