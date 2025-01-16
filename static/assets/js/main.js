// document.addEventListener('scroll', () => {
//   const scrollPosition = window.scrollY;
//   const headerHeight = document.querySelector('header').offsetHeight;

//   // Increase the zoom intensity to 10x
//   const scaleFactor = 1 + (scrollPosition / headerHeight) * 70;

//   const video = document.querySelector('.home-page-main-video');
//   video.style.transform = `scale(${scaleFactor})`; 
// });



// const finalText = "Wide . Sky . International";
// const container = document.getElementById("text");
// const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
// const animationDuration = 2000; // 2 seconds total

// finalText.split('').forEach((targetLetter, index) => {
//   const letterContainer = document.createElement('div');
//   letterContainer.className = 'letter-container';
//   const letterSlot = document.createElement('div');
//   letterSlot.className = 'letter-slot';
//   letterContainer.appendChild(letterSlot);
//   container.appendChild(letterContainer);

//   const iterations = 10 + Math.floor(Math.random() * 5);
//   const iterationDuration = animationDuration / iterations;
  
//   const isEven = index % 2 === 0;
  
//   let currentIteration = 0;
  
//   function updateLetter() {
//     if (currentIteration >= iterations) {
//       letterSlot.textContent = targetLetter;
//       letterSlot.style.animation = `${isEven ? 'slideDown' : 'slideUp'} 0.3s ease-out`;
//       return;
//     }
    
//     const randomLetter = letters[Math.floor(Math.random() * letters.length)];
//     letterSlot.textContent = randomLetter;
//     letterSlot.style.animation = `${isEven ? 'slideDown' : 'slideUp'} 0.3s ease-out`;
    
//     currentIteration++;
//     setTimeout(updateLetter, iterationDuration);
//   }
  
//   setTimeout(() => {
//     updateLetter();
//   }, index * 100);
// });






// Main slider right side of the page
// document.addEventListener('DOMContentLoaded', function () {
//     const elements = document.querySelectorAll('#header, #aboutus, #services, #topclients, #blogs, #contactus, #partners'); 
//     const sliderItems = document.querySelectorAll('.slider-item');
  
//     function updateSlider() {
//         const scrollPosition = window.scrollY;
  
//         elements.forEach((element, index) => {
//             const elementTop = element.offsetTop;
//             const elementBottom = elementTop + element.offsetHeight;
  
//             if (scrollPosition >= elementTop && scrollPosition < elementBottom) {
//                 sliderItems.forEach(item => item.classList.remove('active'));
//                 sliderItems[index].classList.add('active');
//             }
//         });
//     }
  
//     sliderItems.forEach((item, index) => {
//         item.addEventListener('click', function () {
//             const targetElement = elements[index];
//             window.scrollTo({
//                 top: targetElement.offsetTop,
//                 behavior: 'smooth'
//             });
//         });
//     });
  
//     window.addEventListener('scroll', updateSlider);
// });



document.addEventListener('DOMContentLoaded', function () {
    const elements = document.querySelectorAll('#header, #aboutus, #services, #topclients, #blogs, #contactus, #partners'); 
    const sliderItems = document.querySelectorAll('.slider-item');
    let isScrolling = false; // Flag to temporarily disable updateSlider
  
    function updateSlider() {
        if (isScrolling) return; // Skip updating during smooth scrolling

        const scrollPosition = window.scrollY;

        elements.forEach((element, index) => {
            const elementTop = element.offsetTop;
            const elementBottom = elementTop + element.offsetHeight;

            if (scrollPosition >= elementTop && scrollPosition < elementBottom) {
                sliderItems.forEach(item => item.classList.remove('active'));
                sliderItems[index].classList.add('active');
            }
        });
    }

    sliderItems.forEach((item, index) => {
        item.addEventListener('click', function () {
            isScrolling = true; // Disable updateSlider temporarily

            const targetElement = elements[index];
            window.scrollTo({
                top: targetElement.offsetTop,
                behavior: 'smooth'
            });

            // Manually set the active state
            sliderItems.forEach(item => item.classList.remove('active'));
            sliderItems[index].classList.add('active');

            // Re-enable updateSlider after scrolling is done
            setTimeout(() => {
                isScrolling = false;
            }, 1000); // Adjust timeout based on animation duration
        });
    });

    window.addEventListener('scroll', updateSlider);
});
