window.onload = () => {
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
  fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
          const movies = data.results;
          const listElement = document.getElementById('list_movies');
          movies.forEach(movie => {
              const listItem = document.createElement('li');
              listItem.innerText = movie.title;
              listElement.appendChild(listItem);
          });
      })
      .catch(error => console.error('Error fetching movies:', error));
};
