
try:
    import os
    import sys
    import datetime
    import time
    import boto3
    import threading
    from boto3.dynamodb.conditions import *
    print("All Modules Loaded ...... ")
except Exception as e:
    print("Error {}".format(e))
    
def itemValue(dbInstance,SensorKey):
    response = dbInstance.table.query(
        KeyConditionExpression=Key('FaceID').eq(SensorKey))
    
    for i in response['Items']:
        print("Name is:", i['NameID'], " - FaceID is: ", i['FaceID'], " - Volume of cup is: ", i['LiquidVolume'])
    
    return response    

def main():
    global counter
    global SensorKey
    SensorKey = str(counter)

    threading.Timer(interval=7, function=main).start()
    obj = MyDb()
    LiquidVolume='44'
    NameID='Barack Obama'
    if(counter == 1):
        LiquidVolume='45'
        NameID='Donald Trump'
    if(counter == 2):
        LiquidVolume='46'
        NameID='Joe Biden'
    if(counter == 3):
        LiquidVolume='47'
        NameID='Yann'
    if(counter == 4):
        LiquidVolume='48'
        NameID='Jeffrey'
    if(counter == 5):
        LiquidVolume='49'
        NameID='Faizan'
    if(counter == 6):
        LiquidVolume='50'
        NameID='Amarnath'

######### Populate table    
    #obj.put(FaceID=str(counter), LiquidVolume=LiquidVolume, NameID=NameID)

######### Delete Partition Key from table
    #obj.delete(FaceID=str(counter))
    
######### Get all the items in the table ########    
    #tableItem = obj.get
    #print(tableItem)
    
    
######### Print the value from the table column ###########
    data = itemValue(obj)
    for i in data['Items']:
        print("Name is:", i['NameID'], " - FaceID is: ", i['FaceID'], " - Volume of cup is: ", i['LiquidVolume'])
        
    print(f"Uploaded Sample on AWS DynamoDB - FaceID: {counter} Volume: {LiquidVolume} Name: {NameID}")
    counter = counter + 1


#if __name__ == "__main__":
    
