import random
import string


def randomStr(num):
    return "".join(random.sample(string.ascii_letters + string.digits, num))


if __name__ == "__main__":
    print(randomStr(6))
