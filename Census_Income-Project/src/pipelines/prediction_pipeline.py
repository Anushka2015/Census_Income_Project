import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(self,
                 Age:float,
                 workclass:str,
                 education :str,
                 education_num:float,
                 relationship:str,
                 marital_status:str,
                 occupation :str,
                 race:str,
                 sex:str,
                 capital_gain:float,
                 hours_per_week  :float,
                 native_country:str):
        
        
        self.Age=Age
        self.workclass=workclass
        self.education =education 
        self.education_num=education_num
        self.relationship=relationship
        self.marital_status = marital_status
        self.occupation= occupation
        self.race = race
        self.sex = sex
        self.capital_gain = capital_gain
        self.hours_per_week= hours_per_week
        self.native_country= native_country
    

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Age':[self.Age],
                'workclass':[self.workclass],
                'education':[self.education ],
                'education-num':[self.education_num],
                'relationship':[self.relationship],
                'marital-status':[self.marital_status],
                'occupation':[self.occupation],
                'race':[self.race],
                'sex':[self.sex],
                'capital-gain':[self.capital_gain],
                'hours-per-week':[self.hours_per_week],
                'native-country':[self.native_country],
                
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
        
        
