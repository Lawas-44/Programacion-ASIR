# Cuenta de 1 a limit saltando de step en step
def count_step(limit, step):
    result = []
    for i in range(1, limit + 1, step):
        result.append(str(i))
    return "\n".join(result)

def main():
    limit = int(input("Final: "))
    step = int(input("Salt: "))
    output = count_step(limit, step)
    print(output)

if __name__ == "__main__":
    main()