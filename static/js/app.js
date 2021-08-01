const timerElement = document.querySelector("#timer")
const progressBar = document.querySelector("#progressBar")

let timerCounter = progressBar.max;

const interval = setInterval(() => {
    page = window.location.href.split("/").slice(-1)
    
    if (timerCounter <= 1) {
        if (page == "study") {
            window.location.href = "/break";
        } else if (page == "break") {
            window.location.href = "/study";
        }

        clearInterval(interval);
    }
    // timerCounter = 2m
    // timerCounterSeconds = 120
    timerCounter = timerCounter - 1;

    timerDispalyMinutes = Math.floor(timerCounter / 60);
    timerDisplaySeconds = timerCounter % 60;

    timerElement.innerText = timerDispalyMinutes + 'm ' + timerDisplaySeconds + 's';
    progressBar.value = timerCounter;
}, 1000)