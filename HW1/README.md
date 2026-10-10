# HW1: Sales Tax Trap

## The Problem

Okay so imagine you're working the register at a store and you need to write a program that figures out what a customer actually pays. The store's policy is that you take 15% off as a loyalty discount first, and then you add 8% sales tax on top of whatever the discounted price ends up being. You're given these starting values:

```python
subtotal = 84.00
discount_percent = 15
tax_percent = 8
```

Your job is to write a program that correctly calculates and prints `final_total`, which is the amount the customer actually ends up paying. Then, on top of that, write a second version of the calculation that's intentionally wrong, kind of like something a careless programmer might accidentally write. Maybe they mix up the percentage and the decimal rate, or maybe they apply the tax before the discount instead of after. Print that wrong result too, and leave a comment explaining exactly why the two versions give different answers.

## What This Is Supposed to Test and Why

Honestly this problem is testing something I messed up myself when I was working on the restaurant.py assignment. It's checking whether you remember to actually convert a percentage into a decimal before using it in a calculation, since something like 15 and 0.15 look kind of similar but give wildly different results if you're not paying attention. It's also testing whether you can take a word problem and translate the order of the steps correctly into code, since applying the discount before the tax versus after the tax actually changes the final number. I think the hardest part for most people my age taking this class would be resisting the urge to just cram everything into one line of code without stopping to check what units each number is actually in. By making people write a wrong version on purpose and explain why it's wrong, it kind of forces you to actually understand the mistake instead of just avoiding it by luck.

## Answer Key

See [`sales_tax_trap.py`](sales_tax_trap.py).

The correct total comes out to $77.11, and the wrong version spits out $552.00, which really shows how much of a difference that one small mistake makes.
