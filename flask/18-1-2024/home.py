from flask import Flask,render_template,request

app=Flask(__name__)
books=[
    {"id":1,"title":"You Can","author":"George Mathew adams"},
    {"id":2,"title":"The Secret of success","author":"William walker"},
    {"id":3,"title":"The Psychology of life","author":"Anirudha singh"}
]

@app.route("/books",methods=["GET"])
def getbook():
    return books


@app.route("/books/<int:book_id>", methods=["GET"])
def id(book_id):
        for book in books:
            if book["id"]==book_id:
                return book
           
        return {"error":"Book not found"}

@app.route("/newbook",methods=["GET","POST"])
def new():
    if request.method=="POST":
        new_books=  {"id":len(books)+1,
                     "title":request.form["title"],
                     "author":request.form["author"]}
        books.append(new_books)
        return books
    else:
        return render_template("home.html")
    
@app.route("/update/<updatedvalue>",methods=["GET","POST","PUT"])
def update_details(updatedvalue):
    if request.method=="POST":
        updatedbooks={"id":int(request.form["id"]),
                    
                     "title":request.form["title"],
                     "author":request.form["author"]}
 
        books[int(updatedvalue)]=updatedbooks
        return books
    else:
        value=books[int(updatedvalue)]
        return render_template("update.html", value=value)
    
@app.route("/delete/<int:deletevalues>")
def deletebook(deletevalues):
    for i in books:
        if i["id"]==deletevalues:
            books.remove(i)
            return books
            
    else:
        return "Error"
    
# @app.route("/addbooks",methods=["POST"])
# def createbook():
#     # if request.method=="POST":
#     #     newbook={"id":len((books)+1),
#     #          "title":}
#     #     books.append(newbook)
    
#     return addbooks

if __name__=="__main__":
    app.run(debug=True)
    