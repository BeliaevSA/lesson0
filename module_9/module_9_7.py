def is_prime(func):
  def wrapper(num_1, num_2, num_3):
    sum = func(num_1, num_2, num_3)
    is_prime = "Простое"
    for i in range(2, sum):
      if sum % i:
        is_prime = "Составное"
        
    return is_prime
  
  return wrapper

@is_prime
def sum_three(num_1, num_2, num_3):
  return num_1 + num_2 + num_3


result = sum_three(2, 3, 6)
print(result)
