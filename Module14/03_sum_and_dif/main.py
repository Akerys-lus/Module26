num = int(input('Введите число: '))

def summ_num(num):
  summ = 0
  while num > 0:
    n = num % 10
    summ += n
    num //= 10
  return summ

def count_num(num):
  count = 0
  while num > 0:
    count += 1
    num //= 10
  return count



subtraction = summ_num(num) - count_num(num)
print('\nСумма цифр числа:', summ_num(num), '\nКол-во цифр в числе:', count_num(num), '\nРазность суммы и кол-ва цифр:', subtraction)