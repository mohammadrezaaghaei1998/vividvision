// Add event listener to each round button
document.querySelectorAll('.round-button').forEach((button) => {
    button.addEventListener('click', function() {
        const modal = document.getElementById('videoModal');
        const modalVideo = document.getElementById('modalVideo');
        
        const gridItem = button.closest('.video-col');
        const videoElement = gridItem.querySelector('video');
        const videoSource = videoElement.querySelector('source').src;

        videoElement.pause();

        modal.style.display = "block";
        modalVideo.src = videoSource; 
        modalVideo.play(); 
    });
});




document.querySelector('.close').addEventListener('click', function() {
    const modal = document.getElementById('videoModal');
    const modalVideo = document.getElementById('modalVideo');
    modal.style.display = "none"; 
    modalVideo.pause(); 
    modalVideo.src = ""; 
});

window.onclick = function(event) {
    const modal = document.getElementById('videoModal');
    if (event.target == modal) {
        modal.style.display = "none"; 
        const modalVideo = document.getElementById('modalVideo');
        modalVideo.pause(); 
        modalVideo.src = "";
    }
};









    $(document).ready(function(){
        $('.filters-button-group .button').on('click', function(){
            var filterValue = $(this).attr('data-filter');

            $('.filters-button-group .button').removeClass('is-checked');
            $(this).addClass('is-checked');

            if(filterValue === '*') {
                $('.grid-item').show(); 
            } else {
                $('.grid-item').hide(); 
                $(filterValue).show(); 
            }
        });
    });






// Modal
    // function openModal(imageUrl) {
    //     const modal = document.getElementById("imageModal");
    //     const modalImage = document.getElementById("modalImage");
        
    //     modal.style.display = "block";
    //     modalImage.src = imageUrl;
    // }
    
    // function closeModal() {
    //     const modal = document.getElementById("imageModal");
    //     modal.style.display = "none"; 
    // }
    
    // window.onclick = function(event) {
    //     const modal = document.getElementById("imageModal");
    //     if (event.target === modal) {
    //         closeModal();
    //     }
    // };





// right to left transition for galley image  

// function filterImages(category) {
//     const items = document.querySelectorAll('.grid-container div');
    
//     let delay = 0;

//     items.forEach((item, index) => {
//         item.style.transitionDelay = "0s";
//         item.classList.add('rtl-transition');
        
//         if (category === 'all' || item.classList.contains(category)) {
//             item.classList.remove('hidden');

//             item.style.transitionDelay = `${delay}s`;
//             delay += 0.09; 
//         } else {
//             item.classList.add('hidden');
//             item.style.transitionDelay = "0s"; 
//         }

//         setTimeout(() => item.classList.remove('rtl-transition'), 50);
//     });
// }
  // Open modal and play video
//   function openModal(videoUrl) {
//     const modal = document.getElementById('videoModal');
//     const modalVideo = document.getElementById('modalVideo');
//     modalVideo.src = videoUrl;  
//     modal.style.display = 'block';
//     modalVideo.play();  
// }


// function closeModal() {
//     const modal = document.getElementById('videoModal');
//     const modalVideo = document.getElementById('modalVideo');
//     modalVideo.pause(); 
//     modalVideo.currentTime = 0; 
//     modal.style.display = 'none';
//     modalVideo.src = ''; 
// }

// window.onclick = function(event) {
//     const modal = document.getElementById('videoModal');
//     if (event.target == modal) {
//         closeModal();
//     }
// }






// fade out transition for galley image  
function filterImages(category) {
    const items = document.querySelectorAll('.grid-container div');
    
    let delay = 0;

    items.forEach((item, index) => {
        item.style.transitionDelay = "0s";
        item.classList.add('fade-transition');
        
        if (category === 'all' || item.classList.contains(category)) {
            item.classList.remove('hidden');

            item.style.transitionDelay = `${delay}s`;
            delay += 0.03; 
        } else {
            item.classList.add('hidden');
            item.style.transitionDelay = "0s"; 
        }

        setTimeout(() => item.classList.remove('fade-transition'), 50);
    });
}