import argparse


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def main():
    parser = argparse.ArgumentParser(description="Simple command-line calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    parser_add = subparsers.add_parser("add", help="Add two numbers")
    parser_add.add_argument("x", type=float)
    parser_add.add_argument("y", type=float)

    # Subtract command
    parser_sub = subparsers.add_parser("subtract", help="Subtract two numbers")
    parser_sub.add_argument("x", type=float)
    parser_sub.add_argument("y", type=float)

    # Multiply command
    parser_mul = subparsers.add_parser("multiply", help="Multiply two numbers")
    parser_mul.add_argument("x", type=float)
    parser_mul.add_argument("y", type=float)

    # Divide command
    parser_div = subparsers.add_parser("divide", help="Divide two numbers")
    parser_div.add_argument("x", type=float)
    parser_div.add_argument("y", type=float)

    args = parser.parse_args()

    if args.command == "add":
        result = add(args.x, args.y)
    elif args.command == "subtract":
        result = subtract(args.x, args.y)
    elif args.command == "multiply":
        result = multiply(args.x, args.y)
    elif args.command == "divide":
        result = divide(args.x, args.y)
    else:
        parser.error("Unknown command")

    print(result)


if __name__ == "__main__":
    main()
