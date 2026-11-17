import sys

def main():
    # Lee la entrada línea a línea hasta END
    for line in sys.stdin:
        line = line.strip()
        if line == "END":
            break
        if not line:
            continue
        
        # El fitxer /etc/passwd separa els camps amb ':'
        parts = line.split(":")
        # Descarta las líneas que no tienen todos los campos
        if len(parts) >= 7:
            username = parts[0]
            home_dir = parts[5]
            shell = parts[6]
            
            if shell == "/bin/bash":
                print(f"{username} ({home_dir})")

if __name__ == "__main__":
    main()