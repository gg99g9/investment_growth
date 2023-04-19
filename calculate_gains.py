# Filename: calculate_gains.py

# global variable
multiplier_amount = 1000000  # The increment at which gain_margin is increased by 1%

def calculate_gains(amount_inv=0.0, gain_margin=0.1):  # default gain_margin is 0.1%
    """
    This is a function to calculate the return gains of an investment.
    :param amount_inv: the amount of money invested
    :param gain_margin: the rate of return the amount invested
    :return: the total gains, total amount invested, and gain margin at the end of the period
    """

    if amount_inv >= 1000:  # check if initial amount invested is greater than or equal to the minimum of $1000

        if amount_inv >= multiplier_amount:  # check if the amount invested is greater than or equal to the multiplier amount

            multiplier = amount_inv // multiplier_amount  # gather the integer value of the division

            gain_margin = round(((gain_margin + multiplier) / 100),
                                3)  # update the gain_margin with the multiplier, and divide by 100 to convert from percent to decimal

        else:  # no changes to gain margin
            gain_margin = round((gain_margin / 100),
                                3)  # divide by 100 to convert from percent to decimal
        total_gains = amount_inv * gain_margin  # calculate the total gain amount

        total_amount_inv = amount_inv + total_gains  # calculate the total amount invested by adding the total amount gained

        return total_gains, total_amount_inv, gain_margin  # return the total gains, total amount invested, and gain margin

    else:
        print(
            "The minimum investment amount is 1000. You cannot use the app. Goodbye.")  # not enough invested to use the app
