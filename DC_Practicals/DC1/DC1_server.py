from xmlrpc.server import SimpleXMLRPCServer
import math

def calculate_factorial(n):
    print(f"Client requested factorial for: {n}")

    if n < 0:
        return "Error: Factorial of negative number doesn't exist."

    return math.factorial(n)

server = SimpleXMLRPCServer(("localhost", 8000))

print("RPC Server is running on port 8000...")

server.register_function(calculate_factorial, "factorial")

server.serve_forever()