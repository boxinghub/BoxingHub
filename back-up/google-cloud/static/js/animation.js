document.addEventListener("DOMContentLoaded", () => {
    const movingImage = document.getElementById('movingImage');
    const punchingBag = document.getElementById('punchingBag');
    let direction = 1;
    const speed = 1.5; // Adjust the speed by changing this value
    const maxX = window.innerWidth * 4 / 7; // Adjust for the image width
    const minX = window.innerWidth * 3 / 7;
    let x = window.innerWidth * 3 / 7;

    // Position the punching bag at maxX
    punchingBag.style.left = `${maxX}px`;

    function animate() {
        x += speed * direction;
        
        if (x >= maxX || x <= minX) {
            direction *= -1; // Change direction
        }

        // Check for collision with punching bag
        if (x >= maxX - 5 && x <= maxX + 5) {
            punchingBag.classList.add('punched');
            setTimeout(() => {
                punchingBag.classList.remove('punched');
            }, 500);
        }

        movingImage.style.left = `${x}px`;

        requestAnimationFrame(animate);
    }

    animate();
});
