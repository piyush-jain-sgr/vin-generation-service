
# https://www.autocheck.com/vehiclehistory/vin-basics

import random
import re

class VinService:
  def getManufacturer(self):
    manufacturer_list = ["HG", "PG", "TY", "RE", "HJ", "KL"]
    rand_idx = random.randrange(len(manufacturer_list))
    return manufacturer_list[rand_idx]

  def getPotrait(self):
     return (self.getBrand()+self.getEngineSize()+self.getType())

  def getBrand(self):
    brand_list = ["BH", "PJ", "TT", "ES", "BK", "MJ"]
    rand_idx = random.randrange(len(brand_list))
    return brand_list[rand_idx]

  def getEngineSize(self):
    return str(random.randrange(10,99))

  def getType(self):
    type_list = ["A", "J", "G", "S", "L", "X"]
    rand_idx = random.randrange(len(type_list))
    return type_list[rand_idx]

  def getAuthenticater(self):
    return "X"
  def getModelYear(self):
    model_year = ["M", "N", "K", "O", "G", "V"]
    rand_idx = random.randrange(len(model_year))
    return model_year[rand_idx]

  def getManufacturerPlant(self):
    plant_list = ["W", "E", "F", "N", "L", "Z"]
    rand_idx = random.randrange(len(plant_list))
    return plant_list[rand_idx]

  def getSerialNumber(self):
    return str(random.randrange(111111, 999999))

  def generateVin(self, inputNumber):
    vinNumbers = []
    for number in range(inputNumber):
      self.aggregateVinParts(number,vinNumbers)
    return vinNumbers

  def aggregateVinParts(self,number,vinNumbers):
    return ( vinNumbers.append(str(number + 1) + self.getManufacturer()+ self.getPotrait()+ self.getAuthenticater()+self.getModelYear()+self.getManufacturerPlant()+self.getSerialNumber()))

  def validateVIN(self,inputVIN):
    return re.search("^[1-9]{1}[A-Za-z]{4}[0-9]{2}[A-Za-z]{4}[0-9]{6}$", inputVIN)