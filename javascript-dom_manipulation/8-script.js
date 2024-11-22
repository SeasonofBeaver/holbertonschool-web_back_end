/* eslint-disable */
document.addEventListener('DOMContentLoaded', () => {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then((response) => response.json())
      .then((data) => {
        const helloElement = document.querySelector('#hello');
        helloElement.textContent = data.hello;
      })
      .catch((error) => {
        console.error('Error fetching greeting:', error);
      });
});