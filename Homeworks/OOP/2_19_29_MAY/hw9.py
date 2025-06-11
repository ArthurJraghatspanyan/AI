# # Task 9: Advantages of Private Fields (__field)

class PublicData:
  def __init__(self, data):
    self.data = data

class PrivateData:
  def __init__(self, data):
    self.__data = data

  def getData(self):
    return self.__data
  
  def setData(self, newData):
    self.__data = newData

publc = PublicData("PublicDataText")
private = PrivateData("PrivateDataText")

print(publc.data)
publc.data = "AnotherPublicData"
print(publc.data)


private.__data = "AnotherPrivateData"   # Private data doesn't change, except of that name mangling happens.
print(private.__data)   # Before assigning it causes an Error.