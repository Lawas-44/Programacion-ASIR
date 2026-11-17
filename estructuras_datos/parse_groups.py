

def main():
    line = input()
    while line != "":
        camps = line.split(":")
        group = camps[0]
        users = camps[3].split(",")

        users_dict = {}
        for user in users:
            if user not in users_dict:
                users_dict[user] = []
            users_dict[user].append(group)

    
    for u, g in users_dict.values():
        print(f"{u}: {g}")


if __name__ == "__main__":
    main()