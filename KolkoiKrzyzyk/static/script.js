
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
            //console.log(board);
            td.appendChild(button);
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }
    computerMove(n);
    return board;
}

function playerClick(event) {
    const buttonId = event.target.id;
    let button=document.getElementById(buttonId);
    button.value="O";
    button.innerHTML="o";
    button.disabled=true;
    let winningLines=victoryLines(n);
    playerMoveMade(buttonId,moves,winningLines);
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
    computerMove(n);
}

function block_table(n){
    for (let i = 1; i <(n*n)+1; i++) {
        let btn=document.getElementById(String(i));
        btn.disabled=true;
    }
}

function playerMoveMade(buttonId, moves,winningLines){
    moves.set(buttonId,"o");

    computerMove(n,winningLines);
    //let winningLines=victoryLines(n);

    if (moves.size>2){
        if(checkWinner(moves,winningLines) === "o"){
            document.getElementById("result").innerHTML="wygrana";
            block_table(n);
        }
        if(checkWinner(moves,winningLines) === "x"){
            document.getElementById("result").innerHTML="przegrana";
            block_table(n);
        }
    }
}

function getRandomFloat(min, max) {
    return Math.floor(Math.random() * (max - min +1) + min);
}

function computerMove(n,winningLines){
    let size=n*n;
    let move;
    if (moves.size===0){
        move= String(getRandomFloat(1,size));
    }
    else {
        for (const line of winningLines) {
            const values = line.map(key => moves.get(key));
            const unique = new Set(values);
            if (unique.has(undefined) && unique.has("x")){
                //let index=getRandomFloat(1,values.length);
                for (let r = 0; r < values.length; r++) {
                    if (values[r] === undefined)
                        move=line[r];
                }

                break;
            }
        }
    }
    let btn=document.getElementById(String(move));
    if(!btn.disabled) {
        btn.disabled=true;
        btn.innerHTML="x";
        moves.set(move,"x");
    }
    //console.log(btn);
    //console.log(move);

}

function checkFilled(move){
    let btn=document.getElementById(move);

    return !!btn.disabled;
}

function computerTurn(moves,winningLines,n){



       //computerMove(n);

    //console.log(checkFilled(move),move);
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
};