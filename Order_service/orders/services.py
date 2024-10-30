from datetime import date
class OrderService:
    @classmethod
    def parse_time(cls, d):
        date_split = d.split('-')
        if len(date_split) != 3:
            return False
        year = int(date_split[0])
        month = int(date_split[1])
        day = int(date_split[2])

        return date(year, month, day)