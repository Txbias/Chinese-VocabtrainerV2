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

    //TODO: Handle errors
    if(username.length === 0) {

    } else if(password.length === 0) {

    } else if(passwordRepeat.length === 0) {

    }

    if(password !== passwordRepeat) {
        //TODO: Handle error
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
            //TODO: Add message for the user

        }
    });
}