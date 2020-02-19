#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # Find maxiumum value within a list
    # Find minimum value within a list
    # Subtract min value from max to recieve maximum profit

    # Doing a selection sort, then subtracting min from max

    # TODO - Order is important, not sorting this list
    # Originally, was sorting list and then subtracting Max from Min
    # However, if the Max was on Day 1, and the Min was on day 5
    # Unable to purchase the Min before the Max

    for i in range(0, len(prices) - 1):
        current_index = i
        smallest_index = current_index
        for j in range(current_index, len(prices)):
            if prices[smallest_index] > prices[j]:
                smallest_index = j

        # Swap
        temp = prices[smallest_index]
        prices[smallest_index] = prices[current_index]
        prices[current_index] = temp

        # Finding max profit
        temp = (prices[-1] - prices[0])

    return temp


arr1 = [10, 7, 5, 8, 11, 9]  # 5, 11 = 6
arr2 = [100, 90, 80, 50, 20, 10]  # 10, 100 = -10
arr3 = [1050, 270, 1540, 3800, 2]  # 2, 3800 = 3530
arr4 = [100, 55, 4, 98, 10, 18, 90, 95, 43,
        11, 47, 67, 89, 42, 49, 79]  # 4, 100 = 94

print("List One: ", find_max_profit(arr1), "6")
print("List Two: ", find_max_profit(arr2), "-10")
print("List Three: ", find_max_profit(arr3), "3530")
print("List Four: ", find_max_profit(arr4), "94")

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
