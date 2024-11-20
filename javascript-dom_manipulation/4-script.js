window.onload = () => {
  const addItemButton = document.getElementById('add_item');
  addItemButton.onclick = () => {
      const listElement = document.querySelector('ul.my_list');
      const listItem = document.createElement('li');
      listItem.innerText = 'Item';
      listElement.appendChild(listItem);
  };
};
