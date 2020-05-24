import random

def gain():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last)

  print(f"{quotes[rnd1]}{quotes[rnd2]}", end='')

if __name__== "__main__":
  gain()
