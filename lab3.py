#lab3
def sequence_difference(sequence_a, sequence_b):
    return list(set(sequence_a) - set(sequence_b))


def main():
    list_a = [1, 2, 3, 2, 4, 5, 2]
    list_b = [2, 5]

    print(f"Результат виконання: {sequence_difference(list_a, list_b)}")


if __name__ == "__main__":
    main()
    