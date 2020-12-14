from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from CommandList import CommandList as CommandList

class Interface:
  
  def __init__(self, user="admin"):
      self.user = user
      self.commandList = CommandList()
      
  def getCommandListInterface(self):
    self.commandList.getCommandListForHelp()
  
def tester():
  interfaceTesting = Interface("yashsehgal")
  interfaceTesting.getCommandListInterface()


if __name__ == "__main__":
    tester()