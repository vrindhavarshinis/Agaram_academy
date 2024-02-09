from flask import Flask,render_template,request
app=Flask(__name__)


list=[
    {"name":"Vrindhavarshini", "age":20,"qualification":"B.com","contactnumber":7904391212},
    {"name":"Harshini", "age":21,"qualification":"B.E","contactnumber":9489600601},
    {"name":"Ram", "age":18,"qualification":"MBA","contactnumber":9787856562},
    {"name":"Krish", "age":16,"qualification":"MCA","contactnumber":9080364936}
    ]

@app.route("/new", methods=["GET","POST"])
def get_newlist():
    if request.method=="POST":
    
        new={"name":request.form["name"],
             "age":int(request.form["age"]),
             "qualification":(request.form["qualification"]),
             "contactnumber":int(request.form["contactnumber"])}
        list.append(new)
        return list
    else:
        return render_template("home.html")

@app.route("/newdata/<int:updatedvalue>", methods=["GET","POST"])
def get_updatedlist(updatedvalue):
    if request.method=="POST":
    
     newlist={"name":request.form["name"],
             "age":int(request.form["age"]),
             "qualification":request.form["qualification"],
             "contactnumber":int(request.form["contactnumber"])}
     list[updatedvalue]=newlist
     return list

    else:
        value=list[updatedvalue]
        return render_template("update.html",value=value)
        
                



if __name__=="__main__":
    app.run (debug=True)
