import re


def mask_cc_number(cc_string, digits_to_keep=4, mask_char='*'):
   cc_string_total = sum(map(str.isdigit, cc_string))

   if digits_to_keep >= cc_string_total:
       print("Not enough numbers. Add 10 or more numbers to the credit card number.")

   digits_to_mask = cc_string_total - digits_to_keep
   masked_cc_string = re.sub('\d', mask_char, cc_string, digits_to_mask)

   return masked_cc_string


print(mask_cc_number("4259 9826 4026 9299"))
print(mask_cc_number("4259 9826 4026 9299"))
print(mask_cc_number("4259 9826 4026 9299"))