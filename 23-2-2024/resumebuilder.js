let myresume={
   skills:[],
   hobbies:[],
   personal_details:{


   },
   education:[
    {
        course_name:"",
        institution_name:"",
        percentage_scored:"",
        Year:""
    },
    {
        course_name:"",
        institution_name:"",
        percentage_scored:"",
        Year:""
    },
    {
        course_name:"",
        institution_name:"",
        percentage_scored:"",
        Year:""
    }
   ]
};
function gen(ele,key,p_key,index,c_key){
    if (p_key){
        myresume[p_key][key]=ele.value
    }
    else if (c_key){
        myresume[key][index][c_key]=ele.value;
    }
    else{
        myresume[key]=ele.value;
    }
    

    preview()
}
function preview(){
    document.getElementById("code").innerHTML=JSON.stringify(myresume,null,4)
}
function addarrays(key,id){
    let value = document.getElementById(id).value
    myresume[key].push(value)
    document.getElementById(id).value=""
    preview()
}

