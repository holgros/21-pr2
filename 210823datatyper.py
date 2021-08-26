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

# vad är klockan om en googol minuter?
# anta att klockan är 15:10 just nu
now_hours = 15
now_minutes = 10
# restdivision för att ta reda på hur många timmar och minuter som tiden förskjuts
googol = 10**100
hours = googol // 60    # antal hela timmar på en googol minuter
offset_hours = hours % 24   # timmars förskjutning (24 timmar = ett dygn)
offset_minutes = googol % 60
# lägg till de förskjutna minuterna
answer_hours = (now_hours + offset_hours)
answer_minutes = now_minutes + offset_minutes
# om mer än 60 minuter har passerat så börja om på en ny timme
if answer_minutes >= 60:
    answer_hours += 1
    answer_minutes %= 60
answer_hours %= 24  # börja om ifall klockan passerat midnatt
time_string = str(answer_hours) + ":" + str(answer_minutes)
print("Klockan är", time_string, "om en googol minuter.")