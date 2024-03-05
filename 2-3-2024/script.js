// let inputbox=document.getElementById("inputbox")
// let lists=document.getElementById("list")
// let listclass=document.getElementById("listclass")





// function addarray(){
//     if (inputbox.value===""){
//         alert("Write something to add")
//     }
//     else{
//         let input=document.createElement("input");
//         input.type="text";
//         input.id="list";
//         input.className="list"
//         input.value="hello"
//         let container=document.createElement("div");

//         input.addEventListener("input",function(){
//             let inputvalue=input.value;
//             container.textContent=inputvalue
//             console.log(inputvalue)
//         });

        
    
       
//         document.createElement("inputbox")==="";
        
//     }
// }
let inputbox=document.getElementById("inputbox");
let listcontainer=document.getElementById("list");
const countvalue=document.getElementById("count");




// let counting=document.getElementById("count")
// let count=counting.textContent

// let countvalue=document.querySelector("count");
// let taskcount=0;
// let displaycount=(taskcount) =>{
//     countvalue.innertext=taskcount;
// }

function addarray(){
   if (inputbox.value ===''){
    alert("You must write Something");
   
    
   }
   
   
   else {
    let li=document.createElement("li");
    li.innerHTML=inputbox.value;
    listcontainer.appendChild(li);
    document.createElement("li") ==="";
   
    if (countvalue.innerText===0){
        countvalue.innerText=0   +  'items total'
    }
    else{
        countvalue.innerText=listcontainer.children.length  +   'items total'
    }
   }
   inputbox.value="";
//   savetolocal()
}
function cancel(){
   
    listcontainer.remove();
    // if (listcontainer.children.length===0){
    //     alert("refresh to add todo")
    // }
    countvalue.innerText=0 +  'items total'
   
    // savetolocal()
   
       
    
    
   
    document.getElementById("list").style.display="block";
  
}


function checked(){
    document.getElementById("task1").style. background-image== url(bright-green-tick-checkmark-icon-free-png.webp);
    // savetolocal()
}
let taskcount=0;
const displaycount=(taskcount)=>{
    countvalue.innerText=taskcount
}
listcontainer.addEventListener("click",function(e){
    if (e.target.tagName ==="LI"){
        e.target.classList.toggle("checked");
        taskcount=Number(1-taskcount )+ "items total";
        
    }
    displaycount(taskcount) 
});

displaycount(taskcount) 

function savetolocal(){
    localStorage.setItem("todo",listcontainer.innerHTML)

}
function get(){
    listcontainer.innerHTML=localStorage.getItem("todo")
}