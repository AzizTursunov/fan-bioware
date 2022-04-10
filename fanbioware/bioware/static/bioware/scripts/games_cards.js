function click_action(e) {
    var teams = document.getElementsByClassName('projects-card__text');
    for (const value of teams) {
        if (e != value && $(value.parentNode).hasClass('active')) {
            $(value.parentNode).removeClass('active');
        }
    }
    $(e.parentNode).toggleClass('active');
};

function changeCardTitle(e) {
    var cards = document.getElementsByClassName('projects-card');
    for (const value of cards) {
        if (value != e.parentNode && ! $(value).hasClass('active')) {
            $(value).addClass('nothover');
        }
    }
};

function rechangeCardTitle(e) {
    var cards = document.getElementsByClassName('projects-card');
    for (const value of cards) {
        if (value != e.parentNode && ! $(value).hasClass('active')) {
            $(value).removeClass('nothover');
        }
    }
};

function changeSlashColor() {
    var slashes = document.getElementById('projects').getElementsByClassName('archive-projects__slash');
    for (const value of slashes) {
        value.style.color = "#898B91";
    }
};


function rechangeSlashColor() {
    var slashes = document.getElementById('projects').getElementsByClassName('archive-projects__slash');
    for (const value of slashes) {
        value.style.color = "#F16622";
    }
};