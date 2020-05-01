# coding = utf-8


def calculate_bonus(profit):
    # list_profit = [1000000, 600000, 400000, 200000, 100000]
    list_profit = [1000000, 600000, 400000, 200000, 100000, 0]
    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    bonus = 0
    bonus1 =0
    profit_copy = profit
    # for i in len(list_profit):
    for i in range(0, 6):
        if profit > list_profit[i]:
            bonus = (profit - list_profit[i]) * rate[i]
            print("基数，利润，百分比，奖金：", list_profit[i], profit-list_profit[i], rate[i], bonus)
            profit = list_profit[i]
            if list_profit[i] == 0:
                bonus1 = (list_profit[i-1] - list_profit[i]) * rate[i]
            else:
                bonus += (list_profit[i] - list_profit[i+1]) * rate[i]
                # print(bonus)
            bonus += bonus1
    print("利润，奖金", profit_copy, bonus)


if __name__ == '__main__':
    profit1 = input("Please input the profit: ")
    calculate_bonus(int(profit1))


