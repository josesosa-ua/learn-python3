import bank
import generic

account = bank.Account("Doe", "1234", 1000.00)

print ("Account instance created:", account)

a = generic.A()
b = generic.B()

a.a_method()
b.b_method()
b.a_method()