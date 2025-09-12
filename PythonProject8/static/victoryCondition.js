function victoryCondition(moves){
    let victory= false
    if (moves.get(1)===moves.get(2)===moves.get(3)){
        victory = true
    }
    if (moves.get(4)===moves.get(5)===moves.get(6)){
        victory = true
    }
    if (moves.get(7)===moves.get(8)===moves.get(9)){
        victory = true
    }
    if (moves.get(1)===moves.get(4)===moves.get(7)){
        victory = true
    }
    if (moves.get(2)===moves.get(5)===moves.get(9)){
        victory = true
    }
    if (moves.get(3)===moves.get(6)===moves.get(9)){
        victory = true
    }
    if (moves.get(1)===moves.get(5)===moves.get(9)){
        victory = true
    }
    return victory;
}