from poisson import PoissonStream
import argparse


def main():
    intensity = 10
    time = 1000

    stream = PoissonStream(intensity, time)
    stream.plot()


if __name__ == "__main__":
    main()
