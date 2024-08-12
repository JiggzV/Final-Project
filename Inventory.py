''' Jeremy Rodriguez'''
''' 1978358'''



import csv
from datetime import datetime

class Item:
    def __init__(self, itemID, manufacturerName, types, price, serviceDate, damaged):
        self.itemID = itemID
        self.manufacturerName = manufacturerName
        self.types = types
        self.price = price
        self.serviceDate = serviceDate
        self.damaged = damaged

#Pull and load all of the manufacturer data
def load_manufacturer_data(filename):
    data = []
    with open(filename) as Manufacturers:
        manufacturers_data = csv.reader(Manufacturers, delimiter = ',')
        for row in manufacturers_data:
            data.append(row)
        return data

#Data load for the item prices
def load_price_data(filename):
    data = []
    with open(filename) as Price:
        itemPrice_data = csv.reader(Price, delimiter = ',')
        for row in itemPrice_data:
            data.append(row)
        return data


# Service Dates Data
def load_service_data(filename):
    data = []
    with open(filename) as ServiceDate:
        Service_data = csv.reader(ServiceDate, delimiter = ',')
        for row in Service_data:
            data.append(row)
        return data
    
#We will be creating a new list from all of the data that we have just pulled

def ItemsList(manufacturers_data, price_data, Service_data):
    invList = []
    for itemID, manufacturerName, types, *rest in manufacturers_data.values():
        if itemID in price_data and itemID in Service_data:
            price = float(price_data.get(itemID[0]))
            serviceDate = serviceDate.get(itemID)
            damaged = "damaged"

            invList.append(Item(itemID, manufacturerName, types, price, serviceDate, damaged))
    return invList


#This segment writes items into a CSV File
''' Should also be defined with each attributed as asked'''

def Itemcsv(filename, invList):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['itemID', 'manufacturerName', 'types', 'price', 'serviceDate', 'damaged']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in invList:
            writer.writerow({
                'itemID': item.item_id,
                'manufacturerName': item.manufacturer,
                'types': item.types,
                'price': item.price,
                'serviceDate': item.serviceDate.strftime('%m/%d/%Y'),
                'damaged': "damaged" if item.damaged else ""
            })


#For neatness, we will sort all of the attributes 

''' This is the simplest way to sort all of the attributes.
We will also use these defined sorting functions later to create csv files for later attributes.'''

def sortManufacturerName(invList):
    return sorted(invList)
def sortTypes(invList):
    return sorted(invList)
def sortserviceDate(invList):
    return sorted(invList)
def sortPrice(invList):
    return sorted(invList)


# We can now define the main function for the management of inventory
def main():
    manufacturers_data = load_manufacturer_data('ManufacturerList.csv')
    itemPrice_data = load_price_data('PriceList.csv')
    Service_data = load_service_data('ServiceDatesList.csv')



    #This is where we will make a new csv file under FullInventory.CSV
    FullInventory = sortManufacturerName('manufacturerName')
    Itemcsv('FullInventory.csv', FullInventory)



    #We are now creating CSVs for three outputs.
    '''For Simplicity, I based the rest of the outputs on the first for no extra coding.'''

    itemDes = set(item.types for item in ItemsList)
    for types in itemDes:
        description = [item for item in ItemsList if item.types == types] #We will base this line for the rest of the CSV files
        LaptopInv = sortTypes(description)
        Itemcsv(f'{types}LaptopInventory.csv', LaptopInv)

    currenttime= datetime.now()
    pastServiceItems = [item for item in ItemsList if item.types if item.serviceDate < currenttime] #Mentioned earlier
    pastServiceInventory = sortserviceDate(pastServiceItems)
    Itemcsv('PastServiceDateInventory.csv', pastServiceInventory)

    itemDamaged = [item for item in ItemsList if item.damaged] #Mentioned earlier as well
    inventoryDamaged = sortPrice(itemDamaged)
    Itemcsv('DamagedInventory.csv', inventoryDamaged)

    if __name__ == "__main__":
        main()
