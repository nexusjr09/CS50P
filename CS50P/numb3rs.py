def main():
    ip_address = input("Enter your IPv4 address: ")
    print(validate(ip_address))


def validate(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False

    for p in parts:
        if not p.isdigit():
            return False
        if len(p) > 1 and p[0] == "0":
            return False
        if not 0 <= int(p) <= 255:
            return False
    return True


if __name__ == "__main__":
    main()
