$(document).ready(function () {
    $('.cover__slider').slick({
        dots: false,
        infinite: true,
        speed: 800,
        slidesToShow: 1,
        slidesToScroll: 1,
        centerMode: false,
        variableWidth: false,
        touchThreshold: 100,
        prevArrow: "<img src='{% static 'bioware/img/svg/game-list_arrow-active.svg' %}' class='slick-prev' alt='prev'>",
        nextArrow: "<img src='{% static 'bioware/img/svg/game-list_arrow-active.svg' %}' class='slick-next' alt='next'>"
    });

    $('.cover__slider').on('beforeChange', function(event, slick, currentSlide, nextSlide){
        let cur_slide = document.querySelector('.slick-active').querySelector('.cover__title-wrap');
        cur_slide.classList.remove('active');
        cur_slide.classList.add('nonactive');

    });

    $('.cover__slider').on('afterChange', function(event, slick, currentSlide, nextSlide){
        let cur_slide = document.querySelector('.slick-active').querySelector('.cover__title-wrap');
        cur_slide.classList.remove('nonactive');
        cur_slide.classList.add('active');
    });

    //ticking machine
    var percentTime;
    var tick;
    var time = 1;
    var progressBarIndex = 0;

    $('.cover__progress-bar-container .cover__progress-bar-line').each(function(index) {
        var progress = "<div class='inProgress inProgress" + index + "'></div>";
        $(this).html(progress);
    });

    function startProgressbar() {
        resetProgressbar();
        percentTime = 0;
        tick = setInterval(interval, 6);
    }

    function interval() {
        if (($('.cover__slider .slick-track div[data-slick-index="' + progressBarIndex + '"]').attr("aria-hidden")) === "true") {
            progressBarIndex = $('.cover__slider .slick-track div[aria-hidden="false"]').data("slickIndex");
            startProgressbar();
        } else {
            percentTime += 1 / (time + 5);
            $('.inProgress' + progressBarIndex).css({
                width: percentTime + "%"
            });
            if (percentTime >= 100) {
                $('.cover__slider').slick('slickNext');
                progressBarIndex++;
                if (progressBarIndex > 2) {
                    progressBarIndex = 0;
                }
                startProgressbar();
            }
        }
    }

    function resetProgressbar() {
        $('.inProgress').css({
            width: 0 + '%'
        });
        clearInterval(tick);
    }
    startProgressbar();
    // End ticking machine

    $('.cover__progress-bar-container').click(function () {
        clearInterval(tick);
        var goToThisIndex = $(this).find("span").data("slickIndex");
        $('.cover__slider').slick('slickGoTo', goToThisIndex, false);
        startProgressbar();
    });

    let cur_slide = document.querySelector('.slick-active').querySelector('.cover__title-wrap');
    cur_slide.classList.add('active');
});