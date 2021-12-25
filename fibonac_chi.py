import itertools
class Fib:    

    class _Fib_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = [0, 0, 1] 
        
        def __next__(self):
            f = self.i[2]
            self.i[0] = self.i[1]
            self.i[1] = self.i[2]
            self.i[2] = self.i[0] + self.i[1]
            return self.i[2]

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib._Fib_iter()


f = Fib()
print(list(itertools.islice(Fib(), 100)))






