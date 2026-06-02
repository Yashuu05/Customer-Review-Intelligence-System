// Rating Interaction
const ratingBlocks = document.querySelectorAll('.rating-block');
const ratingInput = document.getElementById('ratingInput');

ratingBlocks.forEach(block => {
    block.addEventListener('click', () => {
        // Remove active class from all
        ratingBlocks.forEach(b => b.classList.remove('active'));
        // Add to current
        block.classList.add('active');
        // Set hidden input value
        ratingInput.value = block.getAttribute('data-value');
    });
});

// Reset Handler
document.getElementById('clearBtn').addEventListener('click', () => {
    ratingBlocks.forEach(b => b.classList.remove('active'));
    ratingInput.value = '';
});

// Form Submit Handler (Mock)
document.getElementById('feedbackForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const submitBtn = e.target.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerText;
    
    submitBtn.disabled = true;
    submitBtn.innerText = 'Submitting...';
    
    setTimeout(() => {
        alert('Thank you for your feedback! Your response has been recorded.');
        e.target.reset();
        ratingBlocks.forEach(b => b.classList.remove('active'));
        submitBtn.disabled = false;
        submitBtn.innerText = originalText;
    }, 1000);
});
