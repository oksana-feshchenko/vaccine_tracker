import datetime
from datetime import timedelta
from django import template

register = template.Library()


@register.simple_tag
def compare_date(birth_date: datetime, days_to_add: int, actual_date: datetime) -> str:
    days_to_add = int(days_to_add) - 1
    advise = birth_date + timedelta(days=days_to_add)
    if advise >= actual_date.date():
        return "In time"
    else:
        return "Late"
