let current_Vocab;
let currentIndex = 0;
let vocabsArray;

/**
 * Function to load the lesson. Gets only called by onload
 * @param vocabs Array of vocabs
 */
function loadLesson(vocabs) {
    vocabsArray = vocabs;

    if(vocabs.length > 3) {
        displayVocab(vocabs[0]);
    } else {
        // TODO: Handle error
    }
}

/**
 * Displays one vocab to the screen
 * @param vocab An array of of type [german, chinese character, pinyin, id]
 */
function displayVocab(vocab) {

    console.log(vocab);

    current_Vocab = vocab;
    resetButtons();

    //Insert german text
    document.getElementById("german").innerText = vocab[0];

    // Generate random index to decode which button will be the correct one
    let index = getRandomInt(0, 3);

    document.getElementById("cb_" + index).innerText = vocab[1];

    let usedIndices = [];
    usedIndices[0] = currentIndex;

    //Fill others with other characters
    for(let i = 0; i < 4; i++) {
        if(i === index) {
            continue;
        }

        let id = "cb_" + i;
        let vocabsIndex = currentIndex;
        while(usedIndices.includes(vocabsIndex)) {
            vocabsIndex = getRandomInt(0, vocabsArray.length-1);
        }
        usedIndices[i+1] = vocabsIndex;

        document.getElementById(id).innerText = vocabsArray[vocabsIndex][1];

    }

    currentIndex++;
}

/**
 * Gets called when one character button gets clicked.
 * Evaluates whether the correct button was clicked
 * @param index An integer id representing the clicked button
 */
function handleCharacterSelection(index) {
    const id = "cb_" + index;

    const clickedButton = document.getElementById(id);

    // TODO: Check pinyin input

    if(clickedButton.innerText === current_Vocab[1]) {
        // Clicked button was correct

        updateProgressBar();
        if(currentIndex < vocabsArray.length) {
            displayVocab(vocabsArray[currentIndex]);
        } else {
            // TODO: Learning finished
        }
    } else {
        // Clicked button was false
        clickedButton.classList.remove("btn-outline-dark");
        clickedButton.classList.add("btn-outline-danger");
    }

}

/**
 * Sets all button back to black
 */
function resetButtons() {
    for(let i = 0; i < 4; i++) {
        const id = "cb_" + i;
        const clickedButton = document.getElementById(id);

        clickedButton.classList.remove("btn-outline-danger");
        clickedButton.classList.add("btn-outline-dark");
    }
}

/**
 * Generates a random number between min (inclusive) and max (inclusive)
 * @param min
 * @param max
 * @returns {number}
 */
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.ceil(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * Updates the progress bar below the selection buttons
 */
function updateProgressBar() {
    let progressBar = document.getElementById("count_progress");

    let percentage = ((currentIndex) / vocabsArray.length) * 100;
    percentage = Math.round(percentage * 10) / 10;

    progressBar.setAttribute("style", "width: " + String(percentage + "%"));
    progressBar.setAttribute("aria-valuenow", String(currentIndex));

    progressBar.innerText = String(percentage + "%");
}