let word=[2,3,4,5,6];
function storedata(){
   
    let countedname=JSON.stringify(word)
    sessionStorage.setItem("test",countedname)
    
}
function getdata(){
    let localdata=sessionStorage.getItem("test")
    let arraydata=JSON.parse(localdata)
    alert(arraydata)
}
let list=[2,3,6];
function storedata(){
   
    let countedname=JSON.stringify(word)
    localStorage.setItem("details",countedname)
    
}
function getdata(){
    let localdata=localStorage.getItem("details")
    let arraydata=JSON.parse(localdata)
    alert(arraydata)
}
