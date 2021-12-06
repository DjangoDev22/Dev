// nav bar (drop down)

let dropDownMenu = document.querySelector('.menu');
let downIcon = document.querySelector('.icon');

function toggleMenu() {
    if (dropDownMenu.classList.contains('hide')) {
        dropDownMenu.classList.remove('hide');
    } else {
        dropDownMenu.classList.add('hide');
    }
};

downIcon.onclick = toggleMenu;


// side bar (post details page)
let sideDetailMenu = document.querySelector('.share');
let toggleIcon = document.querySelector('.dots_icon');

function toggleSideMenu() {
    if (sideDetailMenu.classList.contains('hide')) {
        sideDetailMenu.classList.remove('hide');
    } else {
        sideDetailMenu.classList.add('hide');
    }
};

toggleIcon.onclick = toggleSideMenu;
