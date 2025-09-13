
let moves = new Map();
const n = 3; // rozmiar planszy

function makeTable(n){
    const table = document.getElementById("gameBoard");
    let board =[]
    for (let r = 0; r < n; r++) {
        const tr = document.createElement("tr");
        for (let c = 0; c < n; c++) {
            const td = document.createElement("td");
            const button = document.createElement("button");
            button.addEventListener("click", playerClick);
            button.id=String(r * n + c+1);
            button.className="my-btn";
            board.push(button);
            td.appendChild(button);
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }
    return board;
}

function playerClick(event) {
    const buttonId = event.target.id;
    let button=document.getElementById(buttonId);
    button.value="O";
    button.innerHTML="O";
    button.disabled=true;
    playerMoveMade(buttonId,moves);
    return button.id;
}

function resetClick() {
    for (let i = 1; i < 10; i++) {
        let btn=document.getElementById(String(i));
        btn.value="";
        btn.innerHTML="";
        btn.disabled=false;
        moves.clear();
    }
    document.getElementById("result").innerHTML="";
}
function block_table(n){
    for (let i = 1; i < 10; i++) {
        let btn=document.getElementById(String(i));
        btn.disabled=true;
    }
}

function playerMoveMade(buttonId, moves){
    moves.set(buttonId,"o");
    if(checkWinner(moves,victoryLines(n)) === "o"){
        document.getElementById("result").innerHTML="wygrana";
    }
    if(checkWinner(moves,victoryLines(n)) === "x"){

        document.getElementById("result").innerHTML="przegrana";
    }
}

// const observer = new MutationObserver((mutations) => {
//     mutations.forEach((mutation) => {
//         if (mutation.attributeName === "value") {
//             //moves(mutation.target.id,move);
//             //console.log(move);
//             //document.getElementById("result").innerHTML="wygrana";
//            // console.log("Wartość guzika zmieniła się na:", mutation.target.value);
//         }
//     });
// });
//btn=document.getElementById("1");
//observer.observe( btn, { attributes: true });
// obserwujemy atrybuty guzika
//observer.observe(btn, { attributes: true });

window.onload = function() {
    makeTable(n);
    document.getElementById("reset").addEventListener("click", resetClick);
    // for (let i = 1; i < 10; i++) {
    //     let btn=document.getElementById(String(i));
    //     btn.addEventListener("click", playerClick);
    //     //observer.observe( btn, { attributes: true });
    // }

    //document.getElementById("1").addEventListener("click", handleClick);
};