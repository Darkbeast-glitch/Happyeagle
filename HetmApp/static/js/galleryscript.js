// JavaScript to handle image click and enlarge effect
const images = document.querySelectorAll('.gallery-image');
const overlay = document.createElement('div');
overlay.classList.add('overlay');
document.body.appendChild(overlay);

images.forEach(image => {
    image.addEventListener('click', () => {
        const enlargedImage = new Image();
        enlargedImage.src = image.src;
        enlargedImage.classList.add('enlarged-image');
        overlay.innerHTML = '';
        overlay.appendChild(enlargedImage);

        // Add a close button
        const closeButton = document.createElement('span');
        closeButton.classList.add('close-button');
        closeButton.innerHTML = '&times;';
        overlay.appendChild(closeButton);

        overlay.style.display = 'flex';

        // Close the overlay when clicking on the close button or anywhere outside the image
        closeButton.addEventListener('click', () => {
            overlay.style.display = 'none';
        });

        overlay.addEventListener('click', (event) => {
            if (event.target === overlay) {
                overlay.style.display = 'none';
            }
        });
    });
});
