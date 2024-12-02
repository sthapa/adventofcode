import os


def safe_report(line: str) -> bool:
  numbers = line.split(' ')
  increasing = False
  decreasing = False
  prior_number = int(numbers[0])
  for number in numbers[1:]:
    number = int(number)
    if number > prior_number:
      increasing = True
    if number < prior_number:
      decreasing = True
    if increasing and decreasing:
      return False
    diff = number - prior_number
    if abs(diff) < 1 or abs(diff) > 3:
      return False
    prior_number = number
  return True

def damper_safe_report(line: str) -> bool:
  numbers = line.split(' ')
  increasing = False
  decreasing = False
  prior_number = int(numbers[0])
  unsafe = False
  for number in numbers[1:]:
    number = int(number)
    if number > prior_number:
      increasing = True
    if number < prior_number:
      decreasing = True
    if increasing and decreasing:
      unsafe = True
    diff = number - prior_number
    if abs(diff) < 1 or abs(diff) > 3:
      unsafe = True
    prior_number = number
  if not unsafe:
    return True

  for i in range(len(numbers)):
    if safe_report(" ".join(numbers[0:i] + numbers[i + 1:])):
      return True
  return False




safe_reports = 0
with open('day2_reports') as f:
  for line in f:
    if safe_report(line):
      safe_reports += 1
print(safe_reports)

safe_reports = 0
with open('day2_reports') as f:
  for line in f:
    if damper_safe_report(line):
      safe_reports += 1
print(f"Damper safe: {safe_reports}")
