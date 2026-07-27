document.addEventListener('DOMContentLoaded', function() {
    var userTypeField = document.querySelector('#id_user_type');
    var regNoField = document.querySelector('#id_registration_no');

    if (!userTypeField || !regNoField) return;

    userTypeField.addEventListener('change', function() {
        var userType = this.value;
        if (!userType) return;

        var url = '/ajax/generate-registration-no/?user_type=' + encodeURIComponent(userType);

        fetch(url)
            .then(function(response) { return response.json(); })
            .then(function(data) {
                if (data.registration_no) {
                    regNoField.value = data.registration_no;
                }
            });
    });
});