def read_lines():
    lines = []
    # Para con una línea vacía o al final del fichero (EOFError)
    try:
        line = input()
        while line != "":
            lines.append(line)
            line = input()
    except EOFError:
        pass
    return lines


def parse_groups(lines):
    users_dict = {}
    for line in lines:
        camps = line.split(":")
        group = camps[0]

        # El cuarto campo tiene los usuarios separados por comas (puede estar vacío)
        for user in camps[3].split(","):
            if user == "":
                continue
            if user not in users_dict:
                users_dict[user] = []
            users_dict[user].append(group)

    return users_dict


def print_groups(users_dict):
    print("{")
    users = sorted(users_dict)
    for i, user in enumerate(users):
        # La última línea no lleva coma
        end = "," if i < len(users) - 1 else ""
        print(f"    '{user}': {users_dict[user]}{end}")
    print("}")


def main():
    lines = read_lines()
    users_dict = parse_groups(lines)
    print_groups(users_dict)


if __name__ == "__main__":
    main()
