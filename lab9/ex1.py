def harmonic_sum(n):
  if n < 2:return 1
  else:return 1 / n + (harmonic_sum(n - 1))

harmonic=int(input("Harmonic : "))
print(harmonic_sum(harmonic))