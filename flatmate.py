import calendar
from fractions import Fraction


class Flatmate:
    """
    Creates a flatmate person object who pay shares of a bill
    """

    def __init__(self, name, days, month):
        self.name = name
        self.days = days
        self.month = month

    def get_days_in_the_month(self):
        try:
            month_index = list(calendar.month_name).index(self.month.capitalize())
            days = calendar.monthrange(2023, month_index)[1]
            return days
        except ValueError:
            return None

    def days_ratio(self, f1_day, f2_day):
        total_days_in_a_month = self.get_days_in_the_month()
        ratio1 = Fraction(f1_day, total_days_in_a_month)
        ratio2 = Fraction(f2_day, total_days_in_a_month)
        result1 = round(float(ratio1), 2)
        result2 = round(float(ratio2), 2)
        return result1, result2

    def calculate_bill(self, bill, f1_day, f2_day):
        flat_mate_ratio1, flat_mate_ratio2 = self.days_ratio(f1_day, f2_day)
        flatmate_1_amount = flat_mate_ratio1 * bill
        flatmate_2_amount = flat_mate_ratio2 * bill
        total_amount = flatmate_1_amount + flatmate_2_amount
        if total_amount > bill:
            remaining = total_amount - bill
            flatmate_2_amount -= remaining
        else:
            remaining_amount = (bill - total_amount) / 2
            flatmate_1_amount += remaining_amount
            flatmate_2_amount += remaining_amount
        return flatmate_1_amount, flatmate_2_amount
