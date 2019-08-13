def generate_n_chars(n, str):
  result = ""
  for x in range(n):
    result += str
  return result

#test
print(generate_n_chars(5, "x"))
print(generate_n_chars(10, "*"))
print(generate_n_chars(2, "Hello"))
