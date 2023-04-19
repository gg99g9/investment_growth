# Filename: functions_optional.py

def format_currency(value, currency="USD"):  # USD equals United States Dollars
    """
    This is a function to format a value into currency style.
    :param value: the original number to be formatted
    :param currency: the 3-digit country code to identify the country's currency
    :return: formatted value and country code
    """
    formatted_value = "${:.2f}".format(value)  # format the value

    return formatted_value, currency  # formatted value with 2 decimal places and 3-digit country currency code
