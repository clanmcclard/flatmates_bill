class Bill:
    """
    Holds the total bill amount and month and year of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Holds the name of each person as well as the number of days they stayed
    Also calculates the share of the total bill each person apys
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        # assign weight to each person according to share of days
        weight = self.days_in_house/(self.days_in_house + flatmate2.days_in_house)

        # take total bill amount by weight
        to_pay = bill.amount * weight

        # round to two digits and return
        return round(to_pay, 2)
