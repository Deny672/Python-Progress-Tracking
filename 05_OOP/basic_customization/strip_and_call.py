class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars
    
    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")
        print(type(args))
        print(type(kwargs))
        return args[0].strip(self.__chars)

s1 = StripChars("?:!.; ")
s2 = StripChars(" ")
res = s1(" Hello World! ")
res2 = s2(" Hello World! ")
print(res)
print(res2)