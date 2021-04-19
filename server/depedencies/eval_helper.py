def checkPrice(count):
  win = False
  price = ''
  for e in count:
    if e == 'juletrae' and count[e] == 10:
      price = '10 Juletræer der udløser 1000000,- '
      win = True
    if e == 'julemand' and count[e] == 9:
      price = price + '9 Julemænd der udløser 50000,-'
      win = True
    if e == 'rensdyr' and count[e] == 8:
      price = price + '8 Rensdyr der udløser 5000,-'
      win = True
    if e == 'tromme' and count[e] == 7:
      price = price + '7 Rensdyr der udløser 1000,-'
      win = True
    if e == 'mistelten' and count[e] == 6:
      price = price + '6 Mistelteen der udløser 200,-'
      win = True
    if e == 'lys' and count[e] == 5:
      price = price + '5 Julelys der udløser 100,-'
      win = True
    if e == 'kugle' and count[e] == 4:
      price = price + '4 Julekugler der udløser 75,-'
      win = True
    if e == 'stjerne' and count[e] == 3:
      price = price + '3 Julestjerner der udløser 50,-'
      win = True
  return win, price


classes = ['','julemand','rensdyr','juletrae','tromme','stjerne','mistelten','lys','kugle']