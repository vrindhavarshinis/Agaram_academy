// let a=20;
// let b=30;
// console.log(a+b)

function getdata(){
    let email=document.getElementById("email_address").value
    console.log(email)
    let password=document.getElementById("pass")
    console.log(password)
}
 function add(){
    let num1=Number(document.getElementById("num_1").value);
    
    let num2=Number(document.getElementById("num_2").value);
    console.log(num1+num2)
 }
function greater(){
    let num1=Number(document.getElementById("value1").value);
    let num2=Number(document.getElementById("value2").value);
    if (num1>num2){
        console.log(num1,"is greater")
    }
    else if(num2>num1){
        console.log(num2, "is greater")
    }
    else if(num1==num2){
        console.log( "Both are equal")
    }
    else if(typeof(num1) != "number"|| typeof(num2)!="number"){
        console.log("undefined")
    }

 }
function oddeven(){
    let num=Number(document.getElementById("num").value);
    if (num%2==0){
        console.log(num, "is an even number")
    }
    if (num%2!=0){
        console.log(num,"is an odd number")
    }
    

}

function cutoff(){
    let tamil=Number(document.getElementById("tamil").value);
    let english=Number(document.getElementById("english").value);
    let maths=Number(document.getElementById("maths").value);
    let physics=Number(document.getElementById("physics").value);
    let chemistry=Number(document.getElementById("chemistry").value);
    let computer=Number(document.getElementById("computer").value);

    

    let tamilenglish=((tamil+english)/2)/4;
    let mathscutoff=(maths)/2;
    let pcc=((physics+chemistry+computer)/3)/4;

    let total=(tamilenglish+mathscutoff+pcc)

    console.log(total)
}

function getebbill(){
    let inputunit=Number(document.getElementById("inputunit").value);

    if (inputunit<=50)
    {
        let amount50=(inputunit*0.5);
        let total50=(amount50)+(amount50*20)/100;
        console.log(total50)
    }
    else if(inputunit<150 || inputunit==150)
    {
        let amount150=(inputunit-50)*0.75;
        let total150=(50*0.5+amount150);
        console.log(total150 + (total150*.2))
    }
    else if(inputunit<250|| inputunit==250)
    {
        let amount250=(inputunit-150)*1.20;
        let total250=((50*0.5)+(100*0.75)+amount250)+(50*0.5+100*0.75+amount250)*1/5
        console.log(total250)
    }
    else if(inputunit>250)
    {
        let total=(inputunit*1.50)+((inputunit*1.50)*1/5)
        console.log(total)
    }

}