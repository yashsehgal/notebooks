from matplotlib import pyplot as plt
import numpy as np
import math as math

from numpy.core.defchararray import index


def computeDistance(x, y):
  return math.sqrt((x**2) + (y**2))

def getMinMaxRatio(d, m):
  return (d / m) * 100

class Points:
  def __init__(self, length):
    self.points = []
    self.x = []
    self.y = []
    self.length = length
    self.maxPoint = 0
    self.minPoint = []
    self.minMaxRatio = 0
    
  def generatePoints(self):
    for count in range(self.length):
      self.x.append(np.random.randint(-self.length, self.length))
      self.y.append(np.random.randint(-self.length, self.length))

      self.points.append((self.x[count], self.y[count]))

  def findMaximumPointDistance(self):
    self.distances = []
    for count in range(len(self.points)):
      self.distances.append(computeDistance(self.x[count], self.y[count]))
    self.maxPoint = max(self.distances)
    # maxDistanceIndex = index(self.maxPoint)
    maxDistanceIndex = self.distances.index(self.maxPoint)
    maxDistancePointX = self.x[maxDistanceIndex]
    maxDistancePointY = self.y[maxDistanceIndex]
    
    self.maxDistancePointCoordinates = [maxDistancePointX, maxDistancePointY]
    
  def computeRatioForMinMax(self):
    self.ratios = []
    for count in range(len(self.points)):
      self.ratios.append(getMinMaxRatio(self.distances[count], self.maxPoint))
    
    self.plotRatioStatus()

  def plotGraph(self):
    plt.scatter(self.x, self.y)
    plt.scatter(self.maxDistancePointCoordinates[0], self.maxDistancePointCoordinates[1])
    plt.title("points")
    plt.show()

  def plotRatioStatus(self):
    plt.plot(self.points, self.ratios)
    plt.title("point MIN-MAX Ratio Status")
    plt.show()
    

def runTestCasesToCheckThePointsFeature():
  num = int(input("enter size> "))
  points = Points(num)

  points.generatePoints()
  points.findMaximumPointDistance()
  points.plotGraph()
  points.computeRatioForMinMax()


if __name__ == '__main__':
  runTestCasesToCheckThePointsFeature()
