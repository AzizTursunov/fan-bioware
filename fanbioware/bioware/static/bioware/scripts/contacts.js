$(document).ready(function(){
    // Edmond studio slider
    $('.slider-edmont').slick({
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 1,
        centerMode: false,
        variableWidth: true,
        touchThreshold: 100,
        prevArrow: "<img src='./img/svg/slider-arrow-right.svg' class='slick-prev' alt='1'>",
        nextArrow: "<img src='./img/svg/slider-arrow-left.svg' class='slick-next' alt='2'>"
    });
    $('.slider-edmont').on('afterChange', function(event, slick, currentSlide, nextSlide){
        var cur_slide = document.getElementById('edmont__active-slide');
        cur_slide.textContent='0'+(currentSlide+1);
    });

    // Austin studio slider
    $('.slider-austin').slick({
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 1,
        centerMode: false,
        variableWidth: true,
        touchThreshold: 100,
        prevArrow: "<img src='./img/svg/slider-arrow-right.svg' class='slick-prev' alt='3'>",
        nextArrow: "<img src='./img/svg/slider-arrow-left.svg' class='slick-next' alt='4'>"
    });
    $('.slider-austin').on('afterChange', function(event, slick, currentSlide, nextSlide){
        var cur_slide = document.getElementById('austin__active-slide');
        cur_slide.textContent='0'+(currentSlide+1);
    });
});