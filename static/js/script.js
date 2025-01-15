const darkMode = document.querySelector('#switch');

const dark = () => {
    document.body.classList.add('dark-mode');
    document.querySelector('.sidebar-sticky').classList.add('dark-mode');
    document.querySelector('.content').classList.add('dark-mode');
    document.querySelector('#tbodyTable').classList.add('text-light');
}

darkMode.addEventListener('click', () => {
    if (darkMode.checked) {
        dark();
        window.localStorage.setItem('darkmode', 'true');
    } else {
        document.body.classList.remove('dark-mode');
        document.querySelector('.sidebar-sticky').classList.remove('dark-mode');
        document.querySelector('.content').classList.remove('dark-mode');
        document.querySelector('#tbodyTable').classList.remove('text-light');
        window.localStorage.removeItem('darkmode');
    }
})

$(function () {
  const initDarkMode = window.localStorage.getItem('darkmode');
    if (initDarkMode === 'true') {
        darkMode.checked = true;
        dark();
    }  
})