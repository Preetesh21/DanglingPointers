import pandas as pd
import json 
from keras.models import model_from_json
import numpy as np 
 
 
def predict(user_id=100):
        ratings_df=pd.read_csv("ratings.csv")
        # load json and create model
        json_file = open('./model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("./model.h5")
        print("Loaded model from disk")

        b_id =list(ratings_df.book_id.unique())
        b_id.remove(10000)
        #Making recommendations for user 100
        book_arr = np.array(b_id) #get all book IDs
        user = np.array([user_id for i in range(len(b_id))])
        pred = loaded_model.predict([book_arr, user])
        pred = pred.reshape(-1) #reshape to single dimension
        pred_ids = (-pred).argsort()[0:5]

        with open("web_book_data.json", "r") as read_it: 
                data = json.load(read_it) 

        d=[]
        for i in pred_ids:
                d.append(data[i])
        return (d)

