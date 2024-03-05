


function checkdata(){
    let username=document.getElementById("name");
    let userid=document.getElementById("email");
    let userpassword=document.getElementById("password")

    if (userid.value==="vv@gmail.com" && userpassword.value==="1234"){
        window.location="home.html"
        let object={}
        object.user_name=username.value;
        object.user_id=userid.value;
        object.user_password=userpassword.value;
        let login=JSON.stringify(object);
        localStorage.setItem("datas",login)
       
        
    
    }
    else {
        window.location.reload()
        
    }
}

function checkauthentication(){
    
     let userinfo=localStorage.getItem("datas");
     let converted=JSON.parse(userinfo)
     if (converted){
        let head=document.getElementById("head")
        head.innerHTML="Welcome" + converted["user_name"]
        
     }
    
    else{
        window.location="login.html"
    }

}
function logout(){
    localStorage.removeItem("object");
    window.location="login.html"
}
