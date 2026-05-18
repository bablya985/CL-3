import Pyro4

uri = input("PYRO:obj_beb425d6d93744859489b694d367200a@localhost:56658")

string_concatenator = Pyro4.Proxy(uri)

str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

result = string_concatenator.concatenate(str1, str2)

print("Concatenated String :", result)