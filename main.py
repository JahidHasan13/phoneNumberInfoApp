# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import carrier
number_info = phonenumbers.parse(number, "CH")
# print(geocoder.country_name_for_number(number_info, "en"))
print(geocoder.description_for_number(number_info, "en"))
carrier_info = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(carrier_info, "en"))
