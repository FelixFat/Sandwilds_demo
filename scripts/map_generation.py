import pickle


def main():
    map = [[29 for _ in range(20)] for _ in range(20)]
    
    with open("./locations/empty.map", "wb") as file:
        pickle.dump(map, file)


if __name__ == '__main__':
    main()