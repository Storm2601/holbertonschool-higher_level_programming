window.onload = () => {
  const updateHeaderButton = document.getElementById('update_header');
  updateHeaderButton.onclick = () => {
      const headerElement = document.querySelector('header');
      headerElement.innerText = 'New Header!!!';
  };
};
