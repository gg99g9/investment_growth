# Filename: calculate_gains_over_time.py

import calculate_gains as cg

def calculate_gains_over_time(amount_inv=0.0, period=12):
    """
    This is a function to calculate the return gains of an investment over a period of time.
    :param amount_inv: the amount of money invested
    :param period: number of months money is invested
    :return: accumulated estimated values and final gain margin for a period
    """

    # call the base `calculate_gains` function
    gains_after_first_period, amount_inv_after_first_period, gain_margin = cg.calculate_gains(amount_inv)

    # calculate the first period values before entering the loop
    total_amount_inv = amount_inv_after_first_period  # the total amount invested by the end of the first period
    total_gains = gains_after_first_period  # the total gains earned by the end of the first period

    # loop through the period to calculate values for each period. 1 to period-1 because the first period gains were already calculated above
    for i in range(1, period):

        # call the 'calculate_gains' function to update values based on the period and total_amount_inv inside the loop
        gains_for_period, amount_inv_for_period, gain_margin = cg.calculate_gains(total_amount_inv)

        # update the total amount invested
        total_amount_inv = amount_inv_for_period

        # update total gains earned
        total_gains += gains_for_period

    # return the final values
    return total_amount_inv, total_gains, period, gain_margin
