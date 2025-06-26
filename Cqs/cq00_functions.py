__Author__ = "730554437"


def mimic(message: str) -> str:
    """Returns the input message"""
    return message


def main() -> None:
    """print result of mimic"""
    message = input("What is your name?")
    print("Hello " + mimic(message))


if __name__ == "__main__":
    main()
