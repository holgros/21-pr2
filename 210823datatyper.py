# heltal
x = 5   		# heltal
y = 3   		# ett till heltal
print(x+y)  	# 8
print(x-y)  	# 2
print(x*y)  	# 15
print(x/y)  	# 1.6666…
print(x // y)   	# 1 (heltalsdivision)
print(x % y)    	# 2 (restdivision)
print(x**y) 	# 125, dvs. 5 upphöjt till 3
print(-x)   	# -5
print(+x)   	# 5
print(abs(y-x))   # 2

# flyttal och komplexa tal
print(float(x)) 	# 5.0
print(int(3.14))  # 3
print(int("3")) 	# 3
z = complex(1, 2) # komplext tal
print(z)    	# (1+2j)
print(z.conjugate())    # (1-2j)
print(z*z)  	# (-3+4j)

# ta reda på vad en datatyp är
x = 1
print(type(x))	# <class 'int'>
y = 3.14
print(type(y))	# <class 'float'>

# Python är ett dynamiskt typat språk, dvs. variabler kan byta datatyp under programmets körning
x = "1"
print(type(x))  # str
x = 1
print(type(x))  # int
# ... vilket kan leda till överraskningar
def double(x):
    print(x+x)
double(1)   # 2
double("1") # 11