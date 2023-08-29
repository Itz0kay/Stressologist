function toggleSidebar() {
    var sidebar = document.querySelector('.sidebar');
    var overlay = document.getElementById('overlay');

    sidebar.classList.toggle('show');
    overlay.classList.toggle('overlay-show');
}
