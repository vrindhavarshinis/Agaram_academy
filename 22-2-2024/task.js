function getgross(){
    let salary=Number(document.getElementById("salary").value);
    let hra;
    let da;
    if (salary<=10000){
      
       hra=salary*1/5
       da=salary*4/5
    }
    else if (salary<=20000){
      
        hra=salary*1/4
        da=(salary*90)/100
     }
     else if(salary>20000){
      
        hra=(salary*30)/100
        da=(salary*95)/100
     }
     
     let total=salary+hra+da
     console.log(total)
 }
 
