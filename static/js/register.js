/**
 * Redirects the user to the login page
 */
function redirectToLogin() {
    const baseUrl = window.location.origin;
    window.location.href = baseUrl + "/";
}

/**
 * Submits the data entered in the input-fields to the server
 */
function submitRegisterData() {
    //Query data from input fields

    const username = $("input.username-field").val();
    const password = $("input.password-field").val();
    const passwordRepeat = $("input.password-repeat-field").val();

    const alert = $("div.alert");
    if(username.length === 0) {
        alert.text("Der Benutzername darf nicht leer sein!");
        displayAlert(alert);
        return;
    } else if(password.length === 0) {
        alert.text("Das Passwort darf nicht leer sein!");
        displayAlert(alert);
        return;
    }

    if(password !== passwordRepeat) {
        passwordsNotIdentical();
        return;
    }


    $.ajax({
        type: "POST",
        url: "register",
        data: {
            "username": username,
            "password": password,
            "passwordRepeat": passwordRepeat
        },
        contentType: "charset=utf-8"
    }).done(function (data) {
        if(data === "true") {
            //Account created successfully

            redirectToLogin();
        } else {
            //Account already exists
            alert.text("Es existiert bereits ein Nutzer mit diesem Namen");
            displayAlert(alert);
        }
    });
}

function passwordsNotIdentical() {
    const alert = $("div.alert");

    alert.text("Beide Passwörter müssen übereinstimmen");
    displayAlert(alert);
}

function displayAlert(alert) {
    alert.removeClass("error-alert-invisible");
    alert.addClass("error-alert-visible");
}