let move = new Map();
function playerClick(event) {
    const buttonId = event.target.id;
    let button=document.getElementById(buttonId);
    button.value="O";
    button.innerHTML="O";
    button.disabled=true;
    moves(buttonId,move);
    return button.id;
}
function resetClick(event) {
    for (let i = 1; i < 10; i++) {
        let btn=document.getElementById(String(i));
        btn.value="";
        btn.innerHTML="";
        btn.disabled=false;
        move.clear();
    }
    document.getElementById("result").innerHTML="";

}

function moves(buttonId,move){
    move.set(buttonId,"o");
    if(victoryCondition(move) === "o"){
        document.getElementById("result").innerHTML="wygrana";
    }
    if(victoryCondition(move) === "x"){

        document.getElementById("result").innerHTML="przegrana";
    }
}

const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.attributeName === "value") {
            //moves(mutation.target.id,move);
            //console.log(move);
            //document.getElementById("result").innerHTML="wygrana";
           // console.log("Wartość guzika zmieniła się na:", mutation.target.value);
        }
    });
});
//btn=document.getElementById("1");
//observer.observe( btn, { attributes: true });
// obserwujemy atrybuty guzika
//observer.observe(btn, { attributes: true });

window.onload = function() {
    for (let i = 1; i < 10; i++) {
        let btn=document.getElementById(String(i));
        btn.addEventListener("click", playerClick);
        observer.observe( btn, { attributes: true });
    }
    document.getElementById("reset").addEventListener("click", resetClick);
    //document.getElementById("1").addEventListener("click", handleClick);
};