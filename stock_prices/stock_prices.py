#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # TODO - Order is important, not sorting this list
    # Originally, was sorting list and then subtracting Max from Min
    # However, if the Max was on Day 1, and the Min was on day 5
    # Unable to purchase the Min before the Max

    min_price_index = prices.index(min(prices))
    max_price_index = prices.index(max(prices))

    for i in range(0, len(prices)):
        if min(prices) < max(prices):
            if min_price_index < max_price_index:
                return max(prices) - min(prices)
            else:
                return

    return prices


arr1 = [10, 7, 5, 8, 11, 9]  # 5, 11 = 6 -- 11 - 5 = 6
arr2 = [100, 90, 80, 50, 20, 10]  # 10, 100 = -10 -- 10 - 20 = -10
arr3 = [1050, 270, 1540, 3800, 2]  # 2, 3800 = 3530 -- 3800 - 270 = 3530
arr4 = [100, 55, 4, 98, 10, 18, 90, 95, 43,
        11, 47, 67, 89, 42, 49, 79]  # 4, 100 = 94 -- 98 - 4 = 94

print("List One: ", find_max_profit(arr1))
print("List Two: ", find_max_profit(arr2))
print("List Three: ", find_max_profit(arr3))
print("List Four: ", find_max_profit(arr4))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
