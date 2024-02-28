$(document).ready(function() {
    // Fetch the translation data from the URL
    $.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
      // Extract the translation of "hello"
      var helloTranslation = data.hello;
      // Display the translation in the HTML tag with id "hello"
      $("#hello").text(helloTranslation);
    });
  });
  