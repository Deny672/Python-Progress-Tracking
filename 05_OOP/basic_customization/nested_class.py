# In the code below we have the Meta class that 
# is in the Women class, it also shows how we can 
# work with the inner class (its attributes, etc.).

class Women:
    title = "Обьект класса для поля title"
    photo = "Обьект класса для поля photo"
    ordering = "Обьект класса для поля ordering"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        ordering = ["id"]
        def __init__(self, access):
            self._access = access
            self.t = Women.title        # It's best not to do that. Do not access attributes of an external class from a nested class.

w = Women('root', '12345')
print(w.ordering)
print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)