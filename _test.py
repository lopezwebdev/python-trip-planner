load_file_in_context("travel.py")

function_defined('estimated_time_rounded')

if(estimated_time_rounded(50.55) != 51): 
  fail_tests("Looks like your function is not rounding correctly. For the value of `50.55` it does not return `51`. Check your logic and make sure you are not rounding to a specific decimal place.")
  
if(estimated_time_rounded(20) != 20): 
  fail_tests("Looks like your function is not rounding correctly. For the value of `20` it does not return `20`. Check your logic and make sure you are not rounding to a specific decimal place.")

if(estimated_time_rounded(2.1) != 2): 
  fail_tests("Looks like your function is not rounding correctly. For the value of `2.1` it does not return `2`. Check your logic and make sure you are not rounding to a specific decimal place.")
  
try:
  estimate
except:
  fail_tests("Did you create a variable named `estimate`?")
  
if estimate < 0:
  fail_tests("Since it represents a period of time, `estimate` should be a positive number.")

pass_tests()
