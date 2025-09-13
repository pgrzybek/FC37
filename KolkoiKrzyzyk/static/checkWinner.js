function checkWinner2(moves,winningLines) {

    for (const line of winningLines) {

        const values = line.map(key => moves.get(key));
        const unique = new Set(values);

        if (unique.size === 1 && !unique.has(null)) {
            return [...unique][0]; // "X" albo "O"
        }
    }
    return null; // brak zwycięzcy
}
function checkWinner(moves,winningLines) {

    for (const line of winningLines) {

        const values = line.map(key => moves.get(key));
        const unique = new Set(values);

        if (unique.size === 1 && !unique.has(null)) {
            return [...unique][0]; // "X" albo "O"
        }
    }
    return null; // brak zwycięzcy
}