from datetime import timedelta


def adjust_for_weekend(date):
    if date.weekday() == 5:  # If Saturday
        return date + timedelta(days=2)
    elif date.weekday() == 6:  # If Sunday
        return date + timedelta(days=1)
    else:
        return date
