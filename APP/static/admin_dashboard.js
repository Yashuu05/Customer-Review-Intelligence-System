// Simple micro-interactions
document.querySelectorAll('button').forEach(btn => {
    btn.addEventListener('mousedown', () => {
        btn.classList.add('scale-[0.98]');
    });
    btn.addEventListener('mouseup', () => {
        btn.classList.remove('scale-[0.98]');
    });
});

// Toggle Active States
const navLinks = document.querySelectorAll('nav a');
navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        navLinks.forEach(l => {
            l.classList.remove('bg-surface-container-high', 'border-l-4', 'border-primary', 'text-primary', 'font-bold', 'border-b-2');
            l.classList.add('text-secondary');
        });
        link.classList.add('bg-surface-container-high', 'text-primary', 'font-bold');
        if(link.parentElement.classList.contains('flex-col')) {
            link.classList.add('border-l-4', 'border-primary');
        } else {
            link.classList.add('border-b-2', 'border-primary');
        }
    });
});
