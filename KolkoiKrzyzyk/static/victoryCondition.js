function victoryCondition(moves){
    let victory="";
    if (moves.get("1") === moves.get("2") && moves.get("2") === moves.get("3")){
        victory = moves.get("1")
        console.log(moves.get("1"));
    }
    /*
    if (moves.get(4)===moves.get(5) && moves.get(5)===moves.get(6)){
        victory = moves.get("4")
    }
    if (moves.get(7)===moves.get(8) && moves.get(8)===moves.get(9)){
        victory = moves.get("4")
    }
    if (moves.get(1)===moves.get(4) && moves.get(4)===moves.get(7)){
        victory = moves.get("1")
    }
    if (moves.get(2)===moves.get(5) && moves.get(5)===moves.get(9)){
        victory = moves.get("2")
    }
    if (moves.get(3)=== moves.get(6) &&moves.get(6)===moves.get(9)){
        victory = moves.get("3")
    }
    if (moves.get(1)=== moves.get(5) && moves.get(5)===moves.get(9)){
        victory = moves.get("1")
    }
    *?
     */
    return victory;
}