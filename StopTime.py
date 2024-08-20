# About:
#   In this mini project, you are given with a target number. You have to stop your timer at target.
  
#   Example:
#     Target = 6
#     Then you have to give input after 6 secs at console.


import time as t
import random as r

class StopTime:
  def __init__(self) -> None:
    self.__st = 0
    self.__end = 0
    self.__num = r.choice(range(1, 11))
    
  def start(self):
    print(f"You have to stop your timer at {self.__num}")
    
    self.__st = t.time()
    
  def stop(self):
    self.__end = t.time() - self.__st
    
    self.res()
  
  def res(self):
    if round(self.__end) == self.__num:
      print(f"Congrats, Your time = {round(self.__end):.2f} ; Target = {self.__num}")
    else:
      print(f"Your time = {round(self.__end):.2f} ; Target = {self.__num}")
      

stoptime = StopTime()

choiceStart = input("Enter anything to start: ")
stoptime.start()

choiceEnd = input("Enter anything to stop: ")
stoptime.stop()