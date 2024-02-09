from flask import Flask,render_template,request
app=Flask(__name__)

list=["hat","mat"]   
 
@app.route("/todo",methods=["GET","POST"])
def todo():
  if request.method=="POST":
    list.append(request.form["item_name"])
  return render_template("todo.html",itemlist=list)


@app.route("/deletetodo/<deletevalue>", methods=["GET","POST"])
def deleteitem(deletevalue):
  list.remove(deletevalue)
  return render_template("todo.html",itemlist=list)

@app.route("/updatetodo/<v_index>", methods=["GET","PUT","POST"])
def updatelist(v_index):
  if request.method=="POST":
    list[int(v_index)]=request.form["updateditem"]
    return render_template("todo.html",itemlist=list)
  else:
    
    value=list[int(v_index)]
    return render_template("updated.html",value=value)



if __name__=="__main__":
    app.run(debug=True)