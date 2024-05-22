$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    $.each(data.results, function (i, res) {
      $('#list_movies').append('<li>' + res.title + '</li>');
    }
    );
  }
);
