const screenWidth = $(window).width();

$(window).resize(function () {
    const curScreenWidth = $(window).width();
    if (curScreenWidth > 1279 && screenWidth < 1280) {
        document.location.reload();
    }
    if (curScreenWidth < 1280 && screenWidth > 1279) {
        document.location.reload();
    }
});

function click_action(e) {
    var teams = document.getElementById('openings').getElementsByClassName('team-item__caption');
    for (const value of teams) {
        if (e != value && $(value).hasClass('active')) {
            $(value).removeClass('active');
        }
    }
    $(e).toggleClass('active');
};

function changeCardTitle(e) {
    var cards = document.getElementById('openings').getElementsByClassName('team-item');
    for (const value of cards) {
        var cur_opening = value.getElementsByClassName('team-item__caption')[0]
        if (value != e && ! $(cur_opening).hasClass('active')) {
            $(value).addClass('nothover');
        }
    }
};

function rechangeCardTitle(e) {
    var cards = document.getElementById('openings').getElementsByClassName('team-item');
    for (const value of cards) {
        var cur_opening = value.getElementsByClassName('team-item__caption')[0]
        if (value != e && ! $(cur_opening).hasClass('active')) {
            $(value).removeClass('nothover');
        }
    }
};

if ($(window).width() < 1280) {
    $('.benefits-slider').slick({
        arrows: false,
        dots: false,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 3,
        centerMode: true,
        variableWidth: true,
        touchThreshold: 100,
    });
}
