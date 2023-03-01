"""Test script"""

import argparse


def hello(name: str) -> None:
    """Print hello message"""
    print(f"Hello {name}!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Your name", type=str)
    args = parser.parse_args()
    hello(args.name)