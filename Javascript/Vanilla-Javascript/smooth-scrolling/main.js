const navbar_links = document.querySelectorAll('.navigation a');

navbar_links.forEach(element => element.addEventListener('click', smoothScroll));

function smoothScroll(event) {
  event.preventDefault();
  var targedId = event.currentTarget.getAttribute('href');
  window.scrollTo({
    top: document.querySelector(targedId).offsetTop,
    behavior: 'smooth'
  });
}