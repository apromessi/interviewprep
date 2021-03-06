import random

# Class which maintains a shuffled and unshuffled list of chars
class Shuffler:
  def __init__(self):
    print "initializing", self
    self._shuffled = []
    self._unshuffled = []

  # add a character to the shuffler
  def addChar(self, char):
    self._unshuffled.append(char)

    charLen = len(self._shuffled)

    shuffleIdx = random.randint(0, charLen)
    if (shuffleIdx == charLen):
      self._shuffled.append(char)
    else:
      self._shuffled.append(self._shuffled[shuffleIdx])
      self._shuffled[shuffleIdx] = char

  # get the unshuffled version of the string
  def getUnshuffledString(self):
    return "".join(self._unshuffled)

  # get the shuffled version of the string
  def getShuffledString(self):
    return "".join(self._shuffled)

inputStr = "abcdefghijklmnopqrstuvwxyz"

shuffler = Shuffler()
for char in inputStr:
  shuffler.addChar(char)

shuffled = shuffler.getShuffledString()
unshuffled = shuffler.getUnshuffledString()

# compare the strings
allFound = True
for char1 in inputStr:
  found = False
  for char2 in unshuffled:
    if (char1 == char2):
      found = True
  if (found == False):
    allFound = False

if (allFound == False):
  print "ALL CHARACTERS WERE NOT FOUND"
else:
  print "UNSHUFFLED:", shuffler.getUnshuffledString()
  print "SHUFFLED:", shuffler.getShuffledString()
  print "ALL CHARACTERS WERE FOUND"