window.onload = () => {
  const toggleHeaderButton = document.getElementById('toggle_header');
  toggleHeaderButton.onclick = () => {
      const headerElement = document.querySelector('header');
      if (headerElement.classList.contains('red')) {
          headerElement.classList.replace('red', 'green');
      } else {
          headerElement.classList.replace('green', 'red');
      }
  };
};
