from subset import Subset

def main():
    backends = []
    for i in range(12):
        backends.append(i)

    result = {}
    subset_size = 3
    for client_id in range(10):
        result[client_id] = Subset(backends=backends, client_id=client_id, subset_size=subset_size)

    for client_id, backend in result.items():
        print("{}: {}".format(client_id+1, backend))

if __name__ == "__main__":
    main()
