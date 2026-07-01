from shipment.logger import logging
from shipment.exception import shippingException
from shipment.utils.main_utils import MainUtils
import sys

# obj = MainUtils()
# data= obj.read_yaml_file("config/model.yaml")
# print(data)

# from shipment.constants import DB_URL
# print(DB_URL)
# from shipment.configuration.mongo_operation import MongoDBOperation
# obj = MongoDBOperation()
# df= obj.get_collection_as_dataframe(db_name="ShipmentDB", collection_name="ShipmentCollection")
# print(df.head())
from shipment.pipline.training_pipeline import TrainPipeline 
obj=TrainPipeline()
obj.run_pipeline()
