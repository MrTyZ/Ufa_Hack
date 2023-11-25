function onEntry(entry) {
    entry.forEach(change => {
      if (change.isIntersecting) {
        change.target.classList.add('element-show');
      }
      else{
        change.target.classList.remove('element-show');
      }
    });
  }
  let options = { threshold: [0.5] };
  let observer = new IntersectionObserver(onEntry, options);
  let elements1 = document.querySelectorAll('.languages_line');
  for (let elm of elements1) {
    observer.observe(elm);
  }