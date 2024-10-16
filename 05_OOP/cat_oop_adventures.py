class PersianCat:
    bread = 'Persian'
    age = 12.0


class SiberianCat:
    pass


class BengalCat:
    bread = 'Bengal'
    age = 2.0


jerry = PersianCat()

tom = SiberianCat()

alan = BengalCat()

print(type(jerry), type(tom), type(alan), sep="\n")

print(isinstance(5, str))