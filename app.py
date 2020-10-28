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
    print(request.args.get("user"))
    ans=predict(int(request.args.get("user")))
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
    #print(req.user)
@app.route('/instatrends')
def insta_predict():
    print("Hello")
    trends = pd.read_csv('scrapped_products/products_from_instagram.csv')
    links = list(trends["Product URL"])
    return render_template('index3.html',len = len(links), objects = links)

@app.route('/bolly')
def bolly_predict():
    print("Hello")
    return 'Bollywood trends'

@app.route('/fashion')
def fashion_predict():
    ans=news()
    print(ans)
    return render_template('index4.html',objects=ans)

if __name__ == "__main__":
    app.run(debug=True)