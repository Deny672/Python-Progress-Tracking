

class Car:
    lenght : int
    height : int
    engine_displacement : int
    weight : int
    top_speed : int
    passenger_seats : int

class Brand(Car):
    name : str
    date_of_create : str
    company_director : str

audi_a5_c4 = Brand(lenght=30)
# setattr(person, 'age', 31)
print(audi_a5_c4.__dict__)  # Output: 31