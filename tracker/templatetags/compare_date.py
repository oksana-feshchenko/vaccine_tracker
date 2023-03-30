from datetime import timedelta
from django import template

from tracker.templatetags.calculate_date import calculate_date

register = template.Library()


@register.simple_tag
def compare_date(birth_date, days_to_add, actual_date):
    days_to_add = int(days_to_add) - 1
    advise = birth_date + timedelta(days=days_to_add)
    print(type(advise))
    print(actual_date)
    # print(advise >= actual_date.)
    if advise >= actual_date.date():
        return "In time"
    else:
        return "Late"
