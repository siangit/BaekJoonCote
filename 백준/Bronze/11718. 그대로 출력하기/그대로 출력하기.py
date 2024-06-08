while True:
    try:
        lines = input()
        print(lines)
    except EOFError:
        break