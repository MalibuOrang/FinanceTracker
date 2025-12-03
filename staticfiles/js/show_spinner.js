document.body.addEventListener('htmx:beforeRequest', function (evt) {
    document.getElementById('spinner').classList.remove('hidden');
});

document.body.addEventListener('htmx:afterRequest', function (evt) {
    document.getElementById('spinner').classList.add('hidden');
});

