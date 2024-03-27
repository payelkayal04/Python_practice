class OverTheLimitException(Exception):
    def __init__(self, msg):
        self.msg = msg


def withdrawl(amount):
    if amount > 10000:
        raise OverTheLimitException("you can not withdraw more than 10000 rs per day")


withdrawl(100000)
