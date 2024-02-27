// script.js
document.addEventListener('DOMContentLoaded', function() {
    M.updateTextFields();
    // Any other initialization code for Materialize components goes here
});

async function loadText(filename) {
        const response = await fetch(`/static/${filename}.txt`);
        const text = await response.text();
        document.getElementById('text').value = text;
        M.updateTextFields(); // Update Materialize input fields
    }

