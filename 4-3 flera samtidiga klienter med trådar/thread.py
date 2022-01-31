# grundläggande om trådar
from multiprocessing import Event
import time
TIME_INTERVAL = 0.2
def print_letters():
    for letter in "abcdefghijklmnopqrstuvwxyzåäö":
        time.sleep(TIME_INTERVAL)
        print(letter)
def print_numbers():
    for number in range(29):
        time.sleep(TIME_INTERVAL)
        print(number)
#print_letters()
#print_numbers()
from _thread import *
print("Startar trådar!")
start_new_thread(print_letters, ())
start_new_thread(print_numbers, ())
time.sleep(30*TIME_INTERVAL)
print("Avslutar programmet!")