import random
import time
import threading

class Server:
    def __init__(self, name):
        self.name = name
        self.active_connections = 0

    def handle_request(self, request_id):
        self.active_connections += 1
        print(f"[{self.name}] Handling request {request_id} | Active: {self.active_connections}")

        time.sleep(random.uniform(0.5, 2))

        self.active_connections -= 1
        print(f"[{self.name}] Completed request {request_id} | Active: {self.active_connections}")


class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def round_robin(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

    def random_choice(self):
        return random.choice(self.servers)

    def least_connections(self):
        return min(self.servers, key=lambda s: s.active_connections)


def simulate_request(lb, request_id, algorithm):
    if algorithm == "round_robin":
        server = lb.round_robin()

    elif algorithm == "random":
        server = lb.random_choice()

    elif algorithm == "least_conn":
        server = lb.least_connections()

    else:
        raise ValueError("Invalid algorithm")

    server.handle_request(request_id)


def main():
    servers = [Server(f"Server-{i}") for i in range(1, 4)]

    lb = LoadBalancer(servers)

    algorithm = input(
        "Choose algorithm (round_robin / random / least_conn): "
    )

    threads = []

    for i in range(1, 11):
        t = threading.Thread(
            target=simulate_request,
            args=(lb, i, algorithm)
        )

        threads.append(t)
        t.start()

        time.sleep(0.3)

    for t in threads:
        t.join()

    print("\nAll requests processed.")


if __name__ == "__main__":
    main()