
document.getElementById('switch').addEventListener('change', function() {
    if (this.checked) {
        document.body.classList.add('dark-mode');
        document.querySelector('.sidebar-sticky').classList.add('dark-mode');
        document.querySelector('.content').classList.add('dark-mode');
    } else {
        document.body.classList.remove('dark-mode');
        document.querySelector('.sidebar-sticky').classList.remove('dark-mode');
        document.querySelector('.content').classList.remove('dark-mode');
    }
});