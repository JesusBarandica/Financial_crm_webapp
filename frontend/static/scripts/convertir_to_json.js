const loginForm = document.getElementById('form_prospectar');
loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(loginForm);
    const json = {};
    for (const [key, value] of formData.entries()) {
        json[key] = value;
    }
    fetch(loginForm.action, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
});
