function checkWinner(moves,winningLines) {

    for (const line of winningLines) {

        const values = line.map(key => moves.get(key));//makes table(n) of values

        const unique = new Set(values);//non unique are removed

        if (unique.size === 1 && !unique.has(undefined)) {
            return [...unique][0]; // "X" albo "O"
        }
    }
    return undefined; // brak zwycięzcy
}