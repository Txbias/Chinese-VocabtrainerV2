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
    // Query data from input fields

    const username = $("input.username-field").val();
    const password = $("input.password-field").val();
    const passwordRepeat = $("input.password-repeat-field").val();

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
        let response = JSON.parse(data);

        if(response.success === false) {
            // The user entered something invalid
            const alert = $("div.alert");

            alert.text(response.error);
            displayAlert(alert);

        } else {
            // Account created successfully
            redirectToLogin()
        }
    });
}

/**
 * Adds and removes one class to the given object to make it visible
 * @param alert
 */
function displayAlert(alert) {
    alert.removeClass("error-alert-invisible");
    alert.addClass("error-alert-visible");
}