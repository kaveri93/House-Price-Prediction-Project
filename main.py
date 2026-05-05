'''
In this file we are going to load the data and develop House price prediction code in oops concept
'''
import sys
import numpy as np
import pandas as pd
import sklearn
from pandas.io.clipboard import clipboard_set
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore")
import pickle
class HPP:
    def __init__(self,path):
        try:
            # Load dataset
            self.path = path
            self.df = pd.read_csv(self.path)
            # drop unnecessary columns
            self.df = self.df.drop(['date','street','statezip'],axis=1)
            self.df['city'] = self.df['city'].map({'Shoreline':0,'Seattle':1,'Kent':2,'Bellevue':3,'Redmond':4,'Maple Valley':5,'North Bend':6,'Lake Forest Park':7,'Sammamish':8,'Auburn':9,'Des Moines':10,'Bothell':11,'Federal Way':12,'Kirkland':13,'Issaquah':14,'Woodinville':15,'Normandy Park':16,'Fall City':17,'Renton':18,'Carnation':19,'Snoqualmie':20,'Duvall':21,'Burien':22,'Covington':23,'Inglewood-Finn Hill':24,'Kenmore':25,'Newcastle':26,'Mercer Island':27,'Black Diamond':28,'Ravensdale':29,'Clyde Hill':30,'Algona':31,'Skykomish':32,'Tukwila':33,'Vashon':34,'Yarrow Point':35,'SeaTac':36,'Medina':37,'Enumclaw':38,'Snoqualmie Pass':39,'Pacific':40,'Beaux Arts Village':41,'Preston':42,'Milton':43}).astype(int)
            self.df['country'] = self.df['country'].map({'USA':0}).astype(int)
            self.X = self.df.iloc[:, 1:] # independent
            self.y = self.df.iloc[:, 0]  # dependent
            self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y,test_size=0.2,random_state=42)
            print(f"Training dataset size: {len(self.X_train)} : {len(self.y_train)}")
            print(f"Testing dataset size: {len(self.X_test)} : {len(self.y_test)}")
        except Exception as e:
            er_type,er_msg,er_line = sys.exc_info()
            print(f"Error in Line Number: {er_line.tb_lineno} : due to :{er_type} and reason was :{er_msg}")

    def training(self):
        try:
            self.Training_data = pd.DataFrame(self.X_train)
            self.Training_data["y_train"]= self.y_train
            self.reg = LinearRegression()
            self.reg.fit(self.X_train,self.y_train)
            self.y_train_predictions = self.reg.predict(self.X_train)
            self.Training_data['y_train_predictions'] = self.y_train_predictions
            # Train Accuracy manually
            numerator = 0
            denominator = 0
            for i in self.Training_data.index:
                numerator = numerator + (self.Training_data['y_train'][i]-self.Training_data['y_train_predictions'][i])**2
                denominator = denominator + ((self.Training_data['y_train'][i]-self.Training_data['y_train'].mean())**2)
            r2_score_value_manually = 1-numerator/denominator
            print(f"Train Accuracy Manually: {r2_score_value_manually}")
            # Train Loss manually
            s=0
            for j in self.Training_data.index:
                s = s + (self.Training_data['y_train'][j]-self.Training_data['y_train_predictions'][j])**2
            print(f"Train Loss Manually: {np.sqrt(s/len(self.Training_data)-1)}")
            print(f"Train Accuracy: {r2_score(self.y_train,self.y_train_predictions)}")
            print(f"Train Loss: {np.sqrt(mean_squared_error(self.y_train,self.y_train_predictions))}")
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f"Error in Line Number: {er_line.tb_lineno} : due to :{er_type} and reason was :{er_msg}")
    def testing(self):
        try:
            self.Testing_data = pd.DataFrame(self.X_test)
            self.Testing_data["y_test"] = self.y_test
            self.y_test_predictions = self.reg.predict(self.X_test)
            self.Testing_data['y_test_predictions'] = self.y_test_predictions
            # Test Accuracy manually
            numerator = 0
            denominator = 0
            for i in self.Testing_data.index:
                numerator = numerator + (
                            self.Testing_data['y_test'][i] - self.Testing_data['y_test_predictions'][i]) ** 2
                denominator = denominator + (
                            (self.Testing_data['y_test'][i] - self.Testing_data['y_test'].mean()) ** 2)
            r2_score_value_manually = 1 - numerator / denominator
            print(f"Test Accuracy Manually: {r2_score_value_manually}")
            # Test Loss manually
            s = 0
            for j in self.Testing_data.index:
                s = s + (self.Testing_data['y_test'][j] - self.Testing_data['y_test_predictions'][j]) ** 2
            print(f"Test Loss Manually: {np.sqrt(s / len(self.Testing_data)-1)}")
            print(f"Test Accuracy: {r2_score(self.y_test, self.y_test_predictions)}")
            print(f"Test Loss: {np.sqrt(mean_squared_error(self.y_test, self.y_test_predictions))}")
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f"Error in Line Number: {er_line.tb_lineno} : due to :{er_type} and reason was :{er_msg}")

    def check_own_data(self):
        try:
            bedrooms=3
            bathrooms=2
            sqft_living=1930
            sqft_lot=11947
            floors=1
            waterfront=0
            view=0
            condition=4
            sqft_above=1930
            sqft_basement=0
            yr_built=1966
            yr_renovated=0
            city=2
            country=0
            print(f"Test point predictions:{self.reg.predict([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,sqft_above,sqft_basement,yr_built,yr_renovated,city,country]])[0]}")
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f"Error in Line Number: {er_line.tb_lineno} : due to :{er_type} and reason was :{er_msg}")

    def saving_model(self):
        try:
            with open("Model.pkl","wb") as f:
                pickle.dump(self.reg,f)
            print(f"-----------Load and check---------")
            with open('Model.pkl','rb') as t:
                model = pickle.load(t)
                bedrooms = 3
                bathrooms = 2
                sqft_living = 1930
                sqft_lot = 11947
                floors = 1
                waterfront = 0
                view = 0
                condition = 4
                sqft_above = 1930
                sqft_basement = 0
                yr_built = 1966
                yr_renovated = 0
                city = 2
                country = 0
                print(f"Loaded model predictions :{model.predict([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,sqft_above,sqft_basement,yr_built,yr_renovated,city,country]])[0]}")
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f"Error in Line Number: {er_line.tb_lineno} : due to :{er_type} and reason was :{er_msg}")



if __name__ == '__main__':
    try:
        path = "House_price_prediction_data.csv"
        obj = HPP(path)
        obj.training()
        obj.testing()
        obj.check_own_data()
        obj.saving_model()
    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        print(f"Error in Line Number: {er_line.tb_lineno} : due to :{er_type} and reason was :{er_msg}")





