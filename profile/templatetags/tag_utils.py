import datetime
from django import template

register = template.Library()


@register.filter("timestamp_to_time")
def convert_timestamp_to_time(timestamp):
    return datetime.date.fromtimestamp(int(timestamp))


@register.filter("split")
def split_string(text: str, separator: str):
    return [res.strip() for res in text.split(separator)]
