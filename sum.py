import os


def sum(num_a: float, num_b: float) -> None:
    print(f"num_a:{num_a}")
    print(f"num_b:{num_b}")
    print(f"sum:{num_a + num_b}")


if __name__ == "__main__":
    NUM_A: float = os.environ.get("NUM_A")
    NUM_B: float = os.environ.get("NUM_B")

    sum(NUM_A, NUM_B)
