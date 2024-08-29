function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculateResult() {
    let display = document.getElementById('display');
    try {
        display.value = eval(display.value);
    } catch (e) {
        display.value = 'Error';
    }
}

document.addEventListener('keydown', function(event) {
    const key = event.key;
    if ((key >= 0 && key <= 9) || key === '.' || key === '+' || key === '-' || key === '*' || key === '/') {
        appendToDisplay(key);
    } else if (key === 'Enter') {
        calculateResult();
    } else if (key === 'Backspace') {
        document.getElementById('display').value = document.getElementById('display').value.slice(0, -1);
    } else if (key === 'Escape') {
        clearDisplay();
    }
});
