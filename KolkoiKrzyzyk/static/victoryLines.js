function victoryLines(n) {
    const lines = [];

    // wiersze
    for (let r = 0; r < n; r++) {
        //(_, i) => String(r * n + i + 1))); funkcja strzalkowa wejsciowe parametry to element and i
        lines.push(Array.from({length: n}, (_, i) => String(r * n + i + 1)));
    }

    // kolumny
    for (let c = 0; c < n; c++) {
        lines.push(Array.from({length: n}, (_, i) => String(i * n + c + 1)));
    }

    // przekątna główna
    lines.push(Array.from({length: n}, (_, i) => String(i * (n + 1) + 1)));

    // przekątna odwrotna
    lines.push(Array.from({length: n}, (_, i) => String((i + 1) * (n - 1))));

    return lines;
}
