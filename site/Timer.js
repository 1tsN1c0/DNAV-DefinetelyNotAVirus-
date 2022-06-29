const inizioMinuti = 5;
let tempo = inizioMinuti * 60;

const countdownEl = document.getElementById('countdown');

// Aggiorna ogni secondo
let refreshIntervalId = setInterval(updateCountdown, 1000);

function updateCountdown() {
    // Approssima un numero giù fino al suo int più vicino
    const minuti = Math.floor(tempo / 60);
    let secondi = tempo % 60;

    secondi = secondi < 10 ? '0' + secondi : secondi;

    countdownEl.innerHTML = `${minuti}: ${secondi}`;
    tempo--;

    // Stoppa il setInterval quando il tempo < 0 per evitare i numeri negativi
    if(tempo < 0){
        clearInterval(refreshIntervalId);
    }

}