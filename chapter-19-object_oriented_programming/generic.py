class A:
    def __init__(self):
        print("Constructor af A")
        self.x = 1337

    def a_method(self):
        print("Method of A with x =", self.x)

class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor of B")
        self.y = 1000
    def b_method(self):
        print("Method of B with self =", self.y)
        print("I also have access to a.x =", self.x)