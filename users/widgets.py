from django.forms import DateTimeInput


class DatePicker(DateTimeInput):
    input_type = 'date'
