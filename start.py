import FullFacialRecognition
import encodingFaces
import BartenderDynamoDB
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
global SensorKey
global counter
counter = 0
SensorKey = str(counter)

class MyDb(object):

    def __init__(self, Table_Name='TheSmartBartender'):
        self.Table_Name=Table_Name

        self.db = boto3.resource('dynamodb')
        self.table = self.db.Table(Table_Name)

        self.client = boto3.client('dynamodb')

    @property
    def scanner(self):
        response = self.table.scan(
            FilterExpression=Attr('LiquidVolume').eq('44')
            )
        return response['Items']
    
    def querying(self):
        response = self.table.query(
            KeyConditionExpression=Key('FaceID').eq(SensorKey)
            )
        return response
    
    def get_item(self):
        response = self.table.get_item(
            Key={
                'FaceID': SensorKey
            }
        )
        return response.get('Item')
    
    def put(self, FaceID='' , LiquidVolume='', NameID=''):
        self.table.put_item(
            Item={
                'FaceID':FaceID,
                'LiquidVolume':LiquidVolume,
                'NameID' :NameID
            }
        )

    def delete(self,FaceID=''):
        self.table.delete_item(
            Key={
                'FaceID': FaceID
            }
        )

    def describe_table(self):
        response = self.client.describe_table(
            TableName='FaceID'
        )
        return response
# main.py

values = BartenderDynamoDB.itemValue(MyDb(),'0')

print(values['Items'])