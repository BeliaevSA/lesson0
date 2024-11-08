def all_variants(text):
  i = 1
  while i <= len(text):
    j = 0
    while j <= len(text) - i:
      yield text[j:j+i]
      j += 1
    i += 1


a = all_variants("abcdefghij")
for i in a:
  print(i)
