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
    print(ans)
    return jsonify(ans)
    #print(req.user)
    
if __name__ == "__main__":
    app.run(debug=True)