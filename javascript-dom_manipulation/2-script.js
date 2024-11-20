window.onload = () => {
  const redHeaderButton = document.getElementById('red_header');
  redHeaderButton.onclick = () => {
      const headerElement = document.querySelector('header');
      headerElement.classList.add('red');
  };
};
