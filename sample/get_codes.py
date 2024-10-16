from token_pcl import codes, get_keyword

print(codes)

print("\nEnter a code or keyword to get the other one.\nCtrl+C to exit.\n")

while True:
    try:
        code = input(">> ")
        if code.isdigit():
            code = int(code)
            print(get_keyword(code))
        else:
            print(codes.get(code, "Not found"))
    except ValueError:
        print("Not a code nor a keyword")
    except EOFError:
        print()
        exit(0)
    except KeyboardInterrupt:
        print()
        exit(0)