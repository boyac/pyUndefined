def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    from datetime import date, timedelta
    date1 = date(*date1)
    date2 = date(*date2)
    return abs(date1 - date2).days 
