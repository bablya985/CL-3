import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

try:
    number = int(input("Enter a number: "))

    result = proxy.factorial(number)

    print(f"Factorial of {number} is: {result}")

except Exception as e:
    print(f"Error: {e}")