from flask import Flask,render_template,request,redirect  
from cs50 import SQL
    

app=Flask(__name__)

db=SQL("sqlite:///froshims.db")




@app.route("/",methods=["POST","GET"])
def index():
    if request.method=="GET":
        return render_template("main.html")
    if request.method=="POST":
        
        x = request.form.get("name")
        if x=="":
            return "Name required"
        y=request.form.get("sport") 
        db.execute("INSERT INTO registrants (name,sport) VALUES(?,?)",x,y)
        
        return redirect("/done")

@app.route("/done")
def done():
    l = db.execute("SELECT * FROM registrants ")
    return render_template("added.html",l=l)


if __name__== "__main__":
    app.run()






        
