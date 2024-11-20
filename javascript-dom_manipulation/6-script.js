window.onload = () => {
  const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => {
          const characterElement = document.getElementById('character');
          characterElement.innerText = data.name;
      })
      .catch((error) => console.error('Error fetching data:', error));
};
