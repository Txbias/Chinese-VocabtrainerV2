
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
        let response = JSON.parse(data);

        if(response.success === false) {
            const alert = $("div.alert");
            alert.text(response.error);
            alert.removeClass("error-alert-invisible");
            alert.addClass("error-alert-visible");
        }  else {
           // Password is correct
           //TODO: Customize learning for each user
           const baseUrl = window.location.origin;
           window.location.href = baseUrl + "/learn";
        }
    });
}