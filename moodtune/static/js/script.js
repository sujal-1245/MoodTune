document.addEventListener('DOMContentLoaded', function() {
    console.log("MoodTune ready! 🚀");

    const form = document.querySelector('form');
    const fileInput = document.querySelector('input[type="file"]');

    if (form && fileInput) {
        form.addEventListener('submit', function(event) {
            if (!fileInput.value) {
                event.preventDefault();
                alert("Please select a photo before submitting!");
            }
        });
    }
});
