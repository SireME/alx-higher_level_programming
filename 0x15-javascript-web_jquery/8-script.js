/*
 Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

All movie titles must be list in the HTML tag UL#list_movies
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
 */

$(() => {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, (data) => {
    $.each(data.results, (index, value) => {
      $('UL#list_movies').append($(`<li>${value.title}</li>`));
    });
  });
});