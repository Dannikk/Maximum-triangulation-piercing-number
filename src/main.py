import argparse


def get_degrees(file_path: str) -> list:
    with open(file_path, 'r') as file:
        n = int(file.readline())
        _degrees = [-1] * n
        for string in file:
            v1, v2, v3 = list(map(int, string.split()))
            _degrees[v1] += 1
            _degrees[v2] += 1
            _degrees[v3] += 1

    return _degrees


def get_max_piercing(_degrees: list) -> int:
    n = len(_degrees)
    i = 0
    max_piercing: int = 0
    counting: bool = False
    counter: int = 0
    stop_index: int = 0
    while True:
        if counting:
            if _degrees[i] == 0:
                max_piercing = max(max_piercing, counter)
                counter = 0
            else:
                counter += _degrees[i]
        else:
            if _degrees[i] == 0:
                stop_index = i
                counting = True

        i = (i + 1) % n
        if i == stop_index:
            max_piercing = max(max_piercing, counter)
            break

    return max_piercing


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Maximum triangulation piercing number")
    parser.add_argument('input', type=str, help='direction to input file')
    parser.add_argument('-out', type=str, help='direction to output file', default='output.txt')
    args = parser.parse_args()
    input_file = args.input
    output_file = args.out
    print(f"File to read triangulation:\t\t{args.input}")
    print(f"File to write triangulation piercing number:\t{args.out}")

    degrees = get_degrees(input_file)
    max_piercing = get_max_piercing(degrees)

    with open(output_file, 'w') as file:
        file.write(str(max_piercing))
