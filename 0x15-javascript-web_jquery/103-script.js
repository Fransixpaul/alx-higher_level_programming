// fetches and prints how to say “Hello” depending on the language
$(document).ready(function() {
    function fetchTranslation() {
        var languageCode = $('#language_code').val();
        $.get(
            'https://www.fourtonfish.com/hellosalut/hello/',
            { lang: languageCode },
            data => $('#hello').text(data.hello)
        );
    }

    // Fetch translation when button is clicked
    $('#btn_translate').click(fetchTranslation);

    // Fetch translation when ENTER key is pressed while input is focused
    $('#language_code').keypress(function(event) {
        if (event.which === 13) { // Enter key code
            fetchTranslation();
            event.preventDefault(); // Prevent form submission if inside a form
        }
    });
});
