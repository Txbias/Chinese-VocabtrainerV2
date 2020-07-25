
function redirectToRegister() {
    const baseUrl = window.location.origin;
    window.location.href = baseUrl + "/register";
}

function submitLoginData() {
    const username = $("input.username-input-field").val();
    const password = $("input.password-input-field").val();

    $.ajax({
        type: "POST",
        url: "login",
        data: {
            "username": username,
            "password": password
        },
        contentType: "charset=utf-8"
    }).done(function(data) {
       if(data === "true") {
           // Password is correct
           //TODO: Customize learning for each user
           const baseUrl = window.location.origin;
           window.location.href = baseUrl + "/learn";
       } else {
         //TODO: Add message for the user
       }
    });
}