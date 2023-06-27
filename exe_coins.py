Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: C:/Users/Lenovo/AppData/Local/Programs/Python/Python39/coins.py ===
>>> coin1=Pound(True)
>>> print(coin1.value)
1.25
>>> coin2=Pound()
>>> print(coin2.value)
1.0
>>> print(coin1.colour)
gold
>>> print(coin2.colour)
gold
>>> 
=== RESTART: C:/Users/Lenovo/AppData/Local/Programs/Python/Python39/coins.py ===
>>> coin1.colour
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    coin1.colour
NameError: name 'coin1' is not defined
>>> print(coin1.colour)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(coin1.colour)
NameError: name 'coin1' is not defined
>>> coin1=Pound()
>>> print(coin1.colour)
gold
>>> coin1.rust()
>>> print(coin1.colour)
greenish
>>> coin1.clean()
>>> print(coin1.colour)
gold
>>> 
==== RESTART: C:/Users/Lenovo/AppData/Local/Programs/Python/Python39/coins.py ====
>>> coin1=Pound()
>>> coin1.flip
<bound method Pound.flip of <__main__.Pound object at 0x000002686CFC69D0>>
>>> coin1.flip()
>>> coin1.heads
False
>>> coin1.flip()
>>> coin1.heads
False
>>> coin1.flip()
>>> coin1.heads
False
>>> coin1.flip()
>>> coin1.heads
True
>>> 
==== RESTART: C:/Users/Lenovo/AppData/Local/Programs/Python/Python39/coins.py ====
>>> coin1=Pound()
>>> del coin1
Coin spent!
>>> 