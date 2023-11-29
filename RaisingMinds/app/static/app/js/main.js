// Count Section
const counts = document.querySelectorAll('.count');
const speed = 50;

function updateCountsOnScroll() {
  counts.forEach((countbox) => {
    const target = Number(countbox.getAttribute('data-target'));
    const count = Number(countbox.innerText);
    const inc = target / speed;
    const rect = countbox.getBoundingClientRect();
    const offset = 100; 

    if (rect.top < window.innerHeight - offset) {
      if (count < target) {
        countbox.innerText = Math.floor(inc + count);
        setTimeout(updateCountsOnScroll, 130);
      } else {
        countbox.innerText = target;
      }
    }
  });
}

window.addEventListener('scroll', updateCountsOnScroll);