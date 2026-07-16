import os


def main():
    print(f"Number of cores are :{os.cpu_count()}")


if __name__=="__main__":
    main()