

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = list(skus)
    items_set = set(items)
    stock = "ABCD"
    prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    special_offer = "AB"

    total = 0
    for item in items_set:
        if item not in stock:
            return -1
        
        amount = items.count(item)
        if item not in special_offer:
            total += (amount * prices.get(item))
        else:
            if item == "A":
                q, rest = divmod(amount, 3)
                total += (q*130 + rest*prices.get(item))
            elif item == "B":
                q, rest = divmod(amount, 2)
                total += (q*45 + rest*prices.get(item))

    return total


#print(checkout("AAAA"))
#print(checkout("BBBB"))
#print(checkout("C"))
#print(checkout("D"))
#print(checkout("ABCD"))
        

        


"""
Our price table and offers: 
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+


Notes: 
 - For any illegal input return -1

In order to complete the round you need to implement the following method:
     checkout(String) -> Integer

Where:
 - param[0] = a String containing the SKUs of all the products in the basket
 - @return = an Integer representing the total checkout value of the items 
 """
