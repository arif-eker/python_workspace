#
#
#

# our iterable class
class Product:

    def __init__(self):
        self.product_ids = ["a5", "a6", "a7", "a8", "a9", "a10"]

    # define __iter__
    def __iter__(self):
        self.__index = -1
        return self

    # define __next__
    def __next__(self):
        self.__index += 1
        if self.__index < len(self.product_ids):
            return self.product_ids[self.__index]
        else:
            raise StopIteration


products = Product()

for prod_id in products:
    print("product id: ", prod_id)

# product id:  a5
# product id:  a6
# product id:  a7
# product id:  a8
# product id:  a9
# product id:  a10
