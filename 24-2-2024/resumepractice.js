let myresume={
    skills:[],
    personaldetails:{

    },
    academicdetails:[
        {
            coursename:"",
            institutionname:"",
            percentagescored:"",
            year:""
        },
        {
            coursename:"",
            institutionname:"",
            percentagescored:"",
            year:""
        },
        {
            coursename:"",
            institutionname:"",
            percentagescored:"",
            year:""
        }
    ]
}

function getresume(element,key,p_key,index,c_key){
    if (p_key){
        myresume[p_key][key]=element.value
        
    }
    else if (c_key)
        myresume[key][index][c_key]=element.value

    else{
        myresume[key]=element.value
    }
    
    preview()
}
function preview(){
    document.getElementById("code").innerHTML=JSON.stringify(myresume,null,4)
}
function addarrays(key,id){
    let data=document.getElementById(id).value
    myresume[key].push(data)
    document.getElementById(id).value=""
    preview()
}