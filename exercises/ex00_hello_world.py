"""My First exercise in Comp110!"""

__author__ = "730554437"


def greet(name: str) -> str:
    """A welcoming first function defintion"""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
