import datetime
from datetime import timedelta
from django import template

register = template.Library()


@register.simple_tag
def calculate_date(birth_date: datetime, days_to_add: str) -> datetime:
    days_to_add = int(days_to_add) - 1
    new_date = birth_date + timedelta(days=days_to_add)
    return (
        new_date.strftime("%B %d, %Y, %I:%M %p")
        .replace("AM", "a.m.")
        .replace("PM", "p.m.")
    )
