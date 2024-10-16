class A:
    def Hello():
        return 'Привет'
    def World():
        return 'Мир!'


print(A.Hello() + " " + getattr(A, 'World')())
