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

// Form Submit Handler
document.getElementById('feedbackForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const submitBtn = e.target.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerText;
    
    submitBtn.disabled = true;
    submitBtn.innerText = 'Submitting...';
    
    const formData = new FormData(e.target);
    
    try {
        const response = await fetch('/submit', {
            method: 'POST',
            body: formData
        });
        
        // Handle text or json response
        let resultMsg = 'Success';
        let isError = false;
        
        const contentType = response.headers.get("content-type");
        if (contentType && contentType.indexOf("application/json") !== -1) {
            const result = await response.json();
            resultMsg = result.message || result.error || 'Submission completed.';
            isError = !response.ok;
        } else {
            resultMsg = await response.text();
            isError = !response.ok;
        }
        
        if (!isError) {
            alert(resultMsg);
            e.target.reset();
            ratingBlocks.forEach(b => b.classList.remove('active'));
        } else {
            alert('Error: ' + resultMsg);
        }
    } catch (error) {
        alert('An error occurred while submitting. Please try again.');
        console.error(error);
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerText = originalText;
    }
});
