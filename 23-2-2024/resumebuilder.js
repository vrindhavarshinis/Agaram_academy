let myresume={
   skills:[],
   hobbies:[],
   personal_details:{
        languages_known:[]

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
   ],
   experience:[
    {
        company_name:"",
        role:"",
        year_of_experience:""
    },
    {
        company_name:"",
        role:"",
        year_of_experience:""
    }

   ],
   projects:[
    {
        title:"",
        year:"",
        role:""
    },
    {
        title:"",
        year:"",
        role:""
    }
   ],
   certifications:[
    {
        certificate_name:"",
        given_institution:""
    },
    {
        certificate_name:"",
        given_institution:""
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
function getlanguage(p_key,c_key,id){
    let value=document.getElementById(id).value
    myresume[p_key][c_key].push(value)
    document.getElementById(id).value=""
    preview()

}

