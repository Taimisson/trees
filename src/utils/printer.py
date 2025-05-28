def print_boxed(title: str):
    width = len(title) + 4
    print("+" + "-" * width + "+")
    print("|  " + title + "  |")
    print("+" + "-" * width + "+")

def print_divider():
    print("\n" + "=" * 50 + "\n") 