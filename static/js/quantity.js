// quantity
var plus  = document.querySelector(".plus"),
    minus = document.querySelector(".minus"),
    show = document.querySelector(".show");

console.log(show)

plus.onclick = function(){
    
    var num = Number(show.value)
    show.value = num +=1
}

minus.onclick = function(){
    
    var num = Number(show.value)
    if (show.value == 1){
        show.value = 1
    }
    else{
        show.value = num -=1

    }
}