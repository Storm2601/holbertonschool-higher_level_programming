window.onload = () => {
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
          const helloElement = document.getElementById('hello');
          helloElement.textContent = data.hello;
      })
      .catch(error => console.error('Error fetching hello:', error));
};
