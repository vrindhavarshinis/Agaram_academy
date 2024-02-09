from flask import Flask,render_template,request
app=Flask(__name__)

data=[
    {"id":1,"name":"Vrindha","age":21},
    {"id":2,"name":"varshini","age":20},
    {"id":3,"name":"Dhanush","age":28},
    {"id":4,"name":"Ram","age":22},
    
]

@app.route("/data")
def index():
    return data

@app.route("/addupdate/<int:updateindex>",methods=["POST","GET","PUT"])
def add_updates(updateindex):
    if request.method=="POST":
        updateddata={"id":int(request.form["id"]),
                     "name":request.form["name"],
                     "age":int(request.form["age"])}
        data[updateindex]=updateddata
        return data
    else:
        value=data[updateindex]
        return render_template("update.html", value=value)
        
        

# @app.route("/addupdate",methods=["POST"])
# def add_updates():
#     name=request.form["name"]
#     age=int(request.form["age"])
    
#     if "id" in request.form:
#         data_id=int(request.form["id"])
#         for item in data:
#             if item["id"]==data_id:
#                 item["name"]=name
#                 item["age"]=age
#             return item
        
#     else:
#         newdata={"id":len(data)+1,"name":name,"age":age}
#         data.append(newdata)
        
#     return 
if __name__=="__main__":
    app.run(debug=True)
            