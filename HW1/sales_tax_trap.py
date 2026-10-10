subtotal = 84.00
discount_percent = 15
tax_percent = 8

# Correct version
discount_rate = discount_percent / 100
tax_rate = tax_percent / 100

after_discount = subtotal * (1 - discount_rate)
final_total = after_discount * (1 + tax_rate)
print("Correct final_total:", final_total)

# Wrong version on purpose
# Mistake: treats discount_percent and tax_percent like they're already
# decimals instead of converting them, and also applies tax to the
# original subtotal instead of the discounted price.
wrong_total = (subtotal - discount_percent) * tax_percent
print("Wrong final_total:", wrong_total)

# Why they're different:
# The correct version divides the percentages by 100 first so they
# actually behave like rates, and it applies the tax after the discount
# like the store policy says. The wrong version skips that conversion
# entirely, so subtracting discount_percent just chops 15 dollars off
# instead of taking off 15%, and multiplying by tax_percent blows the
# number way out of proportion instead of adding a small percentage.
