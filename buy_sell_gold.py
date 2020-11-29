class API():

    def __init__(self):
        # self.dic = [100, 180, 260, 310, 40, 535, 695]
        self.dic = [1, 5, 7, 10, 20, 17, 15, 11]

    def get_num_days(self):
        return len(self.dic)

    def get_price_on_day(self, day):
        return self.dic[day]

class Solution():

    def __init__(self):
        # You can initiate and calculate things here
        self.api = API()
        self.number_of_days = self.api.get_num_days()
        self.prices = []

        for i in range(self.number_of_days):
            self.prices.append(self.api.get_price_on_day(i))

    def get_buy_day(self):
        """
        Return the day which you buy gold. The first day has number zero. This method is
        called first, and only once.


        :rtype: int
        """
        # Write your code here
        profit = 0
        buy_day = 0
        day = 0

        while day < self.number_of_days and day != (self.number_of_days - 1):
            if self.prices[day] < self.prices[day + 1] and abs(self.prices[day] - self.prices[day + 1]) > profit:
                buy_day = day
            day += 1

        return buy_day

    def get_sell_day(self):
        """
        Return the day to sell gold on. This day has to be after (greater than) the buy
        day. The first day has number zero (although this is not a valid sell day). This
        method is called second, and only once.


        :rtype: int
        """
        # Write your code here
        profit = 0
        sell_day = 0
        day = 0

        while day < self.number_of_days and day != (self.number_of_days - 1):
            if self.prices[day] > self.prices[day + 1] and abs(self.prices[day] - self.prices[day + 1]) > profit:
                sell_day = day
                profit = abs(self.prices[day] - self.prices[day + 1])
            day += 1

        return sell_day

sol = Solution()
sol.get_buy_day()
sol.get_sell_day()
