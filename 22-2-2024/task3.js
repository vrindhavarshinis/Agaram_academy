function percentage(){
    let biology=Number(document.getElementById("biology").value);
    let maths=Number(document.getElementById("maths").value);
    let physics=Number(document.getElementById("physics").value);
    let chemistry=Number(document.getElementById("chemistry").value);
    let computer=Number(document.getElementById("computer").value);

    let totalpercentage=(biology+maths+physics+chemistry+computer)
    let total=totalpercentage/5

    if (total>=90){
        console.log( totalpercentage,"Grade A")
    }
    else if (total>=80){
        console.log( totalpercentage,"Grade B")
    }
    else if (total>=70){
        console.log( totalpercentage,"Grade C")
    }
    else if (total>=60){
        console.log( totalpercentage,"Grade D")
    }
    else if (total>=40){
        console.log( totalpercentage,"Grade F")
    }
    else if (total<40){
        console.log( totalpercentage,"Grade F")
    }
    
}