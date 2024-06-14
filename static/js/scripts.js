document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    if (currentTheme === 'dark') {
        document.body.classList.add('dark-mode');
        toggleButton.classList.add('dark-mode');
    } else {
        document.body.classList.add('light-mode');
    }
    
    toggleButton.addEventListener('click', function() {
        if (document.body.classList.contains('dark-mode')) {
            document.body.classList.remove('dark-mode');
            document.body.classList.add('light-mode');
            toggleButton.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
        } else {
            document.body.classList.add('dark-mode');
            document.body.classList.remove('light-mode');
            toggleButton.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
        }
    });
});
