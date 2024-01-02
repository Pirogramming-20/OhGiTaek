function loaditems() {
  return fetch("data/data.json")
    .then((response) => response.json())
    .then((json) => json.items);
}

loaditems()
  .then((items) => {
    //displayItems(items);
    //seteventListeners(items);
  })
  .catch(console.log);