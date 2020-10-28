from flask import Flask,render_template,request,jsonify
from user_recommendation import predict

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
    return 'instatrends'

@app.route('/bolly')
def bolly_predict():
    print("Hello")
    return 'Bollywood trends'

@app.route('/fashion')
def fashion_predict():
    print("Hello")
    return 'Fashion'

if __name__ == "__main__":
    app.run(debug=True)