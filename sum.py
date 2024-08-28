import sys


def sum(num_a: float, num_b: float) -> None:
    print(f"num_a:{num_a}")
    print(f"num_b:{num_b}")
    print(f"sum:{num_a + num_b}")


if __name__ == "__main__":
    NUM_A: float = sys.argv[1]
    NUM_B: float = sys.argv[2]

    sum(NUM_A, NUM_B)
