
document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const helloDiv = document.querySelector('#hello');
      helloDiv.textContent = data.hello;
    })
    .catch(error => console.error('Error:', error));
});
