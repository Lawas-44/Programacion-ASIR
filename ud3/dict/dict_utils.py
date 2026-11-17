def merge_dicts(dict1, dict2):
    # Creamos un diccionario nuevo para no modificar los originales
    merged = {}
    for key, val in dict1.items():
        merged[key] = val
    # Si una clave está en los dos, se queda el valor de dict2
    for key, val in dict2.items():
        merged[key] = val
    return merged

def main():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    print(f"Diccionario 1: {dict1}")
    print(f"Diccionario 2: {dict2}")
    print(f"Combinados: {merge_dicts(dict1, dict2)}")

if __name__ == "__main__":
    main()
