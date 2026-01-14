class ClassWithContext:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("This is my name,", self.name)

    def __enter__(self):
        print("Inside magic enter.")
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        print("Inside magic exit.")