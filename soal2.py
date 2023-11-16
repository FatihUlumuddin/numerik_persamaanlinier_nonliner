# Persamaan Linier
# 2x + 4 = 8
def persamaan_linier(a, b, c):

  x = (c - b) / a
  return x


if __name__ == "__main__":
  a = 2
  b = 4
  c = 8
  x = persamaan_linier(a, b, c)
  print(f"solusi dari persamaan linier 2x + 4 = 8 yaitu, x = {x}")
