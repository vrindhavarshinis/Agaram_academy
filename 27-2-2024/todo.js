
let inputbox=document.getElementById("input");
let listcontainer=document.getElementById("list");
const countvalue=document.getElementById("count");

// let body=document.getElementById('body')


// let counting=document.getElementById("count")
// let count=counting.textContent

// let countvalue=document.querySelector("count");
// let taskcount=0;
// let displaycount=(taskcount) =>{
//     countvalue.innertext=taskcount;
// }

// function enter(){
//     if (Event.key==='Enter'){
//         alert('press an add key')
// }
// }


function addarray(){
   if (inputbox.value ===''){
    alert("You must write Something");
   
    
   }
   
   
   else {
    let li=document.createElement("li");
    li.innerHTML=inputbox.value;
    console.log(li.innerHTML)
    listcontainer.appendChild(li);
    document.createElement("li") ==="";
   
    if (countvalue.innerText===0){
        countvalue.innerText=0   +  '-items total'
    }
    else{
        countvalue.innerText=listcontainer.children.length  +   '-items total'
    }
   }
   inputbox.value="";
//   savetolocal()
}
function cancel(){
   
    listcontainer.remove();
    window.location.reload()
    // if (listcontainer.children.length===0){
        
    // }
    countvalue.innerText=  '0-item total'
   
    // savetolocal()
   
    document.getElementById("list").style.display="block";
  
}
body.addEventListener('click',function(event){
    // event.target.style.background-image="url(.jpg)";
})


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
        alert("checked")
        checkedcount=(1-taskcount)+ "-items total";
        
    }
    
    displaycount(checkedcount)
});

displaycount(taskcount) 

function savetolocal(){
    localStorage.setItem("todo",listcontainer.innerHTML)

}
function get(){
    listcontainer.innerHTML=localStorage.getItem("todo")
}
//  get()
// 
 

// if (listcontainer.children.length===0){
//     countvalue.innerText='${listcontainer.children.length}'
// }

// function refreshui(){
//     countvalue.innerText='${listcontainer.children.length}items total'
//    if (listcontainer.children.length>0){
//     nolist.hidden=false;
//     countvalue.innerText="${istcontainer.children.length} items total"
//    }
   
//    else{
//      nolist.hidden=false;
//     }

// }
// listcontainer.children.length>0
// ?((nolist.hidden=true),(countvalue.hidden=true))
// :((nolist.hidden=false),(countvalue.hidden=false));
// }
