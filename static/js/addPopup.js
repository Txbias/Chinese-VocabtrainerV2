/**
 * Display or hides the modal popup
 */
function toggleModal() {

    const pinyinInput = document.getElementById("pinyin");
    pinyinInput.classList.toggle("pinyin-input-hidden");

    document.getElementById("modal").classList.toggle("show-modal");
    const progressBar = document.querySelector(".progress");
    progressBar.toggleAttribute("hidden");
}

/**
 * Adds the entered vocabulary to the database
 */
function addVocab() {
    const pinyinInput = document.getElementById("pinyin-modal-input");
    const germanInput = document.getElementById("german-modal-input");
    const chineseInput = document.getElementById("chinese-modal-input");


    if(pinyinInput.value.length === 0) {
        pinyinInput.classList.add("modal-input-red");
        return;
    } else {
        pinyinInput.classList.remove("modal-input-red");
    }

    if(germanInput.value.length === 0) {
        germanInput.classList.add("modal-input-red");
        return;
    } else {
        germanInput.classList.remove("modal-input-red");
    }

    if(chineseInput.value.length === 0) {
        chineseInput.classList.add("modal-input-red");
        return;
    } else {
        chineseInput.classList.remove("modal-input-red");
    }

    //TODO: send data to server
    $.ajax({
        type: "POST",
        url: "addVocab",
        data: {
            "pinyin": pinyinInput.value,
            "german": germanInput.value,
            "chinese": chineseInput.value
        },
        contentType: "charset=utf-8"
    });

    toggleModal();
}