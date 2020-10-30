from flask import Flask,render_template,request,jsonify
from user_recommendation import predict
import pandas as pd
from fashion_news import news

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict')
def predicts():
    # print(request.args.get("user"))
    if request.args.get("user"):
        ans=predict(int(request.args.get("user")))
    else:
        ans=predict(100)
    for item in ans :
        final_des = ""
        full_des = item['Descriptions']
        all_des = full_des.split('\'')
        if(len(all_des) == 1):
            final_des = all_des[0]
        else:
            final_des = all_des[1]
        item['Descriptions'] = final_des
    
    return render_template("index2.html",len = len(ans), objects = ans)

@app.route('/instatrends')
def insta_predict():
    trends = pd.read_csv('products.csv')
    ans=[]
    for _,row in trends.iterrows():
        quote = {}  
        quote['url'] = row['Product URL'] 
        quote['tag'] = row['tags']
        ans.append(quote)
    
    return render_template('index3.html',len = len(ans), objects = ans)

@app.route('/bolly')
def bolly_predict():
    # print("Hello")
    return render_template('index5.html')

@app.route('/fashion')
def fashion_predict():
    ans=news()
    # print(ans)
    # for url https://www.vogue.in/
    return render_template('index4.html',len = len(ans),objects=ans)

if __name__ == "__main__":
    app.run(debug=True)