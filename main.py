from adapters.base import get_price
from config import locations


def save_prices():
    for location in locations:
        price = get_price(location)
        import pdb

        pdb.set_trace()


if __name__ == "__main__":
    save_prices()
