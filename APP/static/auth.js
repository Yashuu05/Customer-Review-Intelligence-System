document.addEventListener('DOMContentLoaded', () => {
    // Show/Hide Password functionality
    const toggleButtons = document.querySelectorAll('.toggle-password');
    
    toggleButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const inputId = btn.getAttribute('data-target');
            const inputField = document.getElementById(inputId);
            const icon = btn.querySelector('.material-symbols-outlined');
            
            if (inputField.type === 'password') {
                inputField.type = 'text';
                icon.textContent = 'visibility_off';
            } else {
                inputField.type = 'password';
                icon.textContent = 'visibility';
            }
        });
    });

    // Simple micro-interactions
    document.querySelectorAll('button[type="submit"]').forEach(btn => {
        btn.addEventListener('mousedown', () => {
            btn.classList.add('scale-[0.98]');
        });
        btn.addEventListener('mouseup', () => {
            btn.classList.remove('scale-[0.98]');
        });
    });
});
