$(document).ready(function() {
    // Fetch the movie data from the URL
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
      // Iterate through each movie in the fetched data
      $.each(data.results, function(index, movie) {
        // Extract the title of the movie
        var title = movie.title;
        // Create a new list item element with the movie title
        var listItem = $("<li>").text(title);
        // Append the list item to the UL with id "list_movies"
        $("#list_movies").append(listItem);
      });
    });
  });