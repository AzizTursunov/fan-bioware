$(document).ready(function(){
    $('.slider').slick({
        arrows: false,
        dots: true,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 1,
        centerMode: false,
        variableWidth: true,
        touchThreshold: 100,
    });
});

var video_after_list = new Array();
var video_before_list = new Array();
video_after_list[0] = [
    /*
    "https://media.contentapi.ea.com/content/dam/eacom/mass-effect-legendary-edition/videos/2021/01/mele-comparison-video-me1-le.mp4",
    "https://media.contentapi.ea.com/content/dam/eacom/mass-effect-legendary-edition/videos/2021/01/mele-comparison-video-me1-le.webm",
    */
    '../videos/mass-effect-legendary-edition-first_after.mp4',
    '../videos/mass-effect-legendary-edition-first_after.webm'
];
video_after_list[1] = [
    /*
    "https://media.contentapi.ea.com/content/dam/eacom/mass-effect-legendary-edition/videos/2021/01/mele-comparison-video-me2-le.mp4",
    "https://media.contentapi.ea.com/content/dam/eacom/mass-effect-legendary-edition/videos/2021/01/mele-comparison-video-me2-le.webm",
    */
    '../videos/mass-effect-legendary-edition-second_after.mp4',
    '../videos/mass-effect-legendary-edition-second_after.webm'
];
video_before_list[0] = [
    /*
    "https://media.contentapi.ea.com/content/dam/eacom/mass-effect-legendary-edition/videos/2021/01/mele-comparison-video-me1-og.mp4",
    "https://media.contentapi.ea.com/content/dam/eacom/mass-effect-legendary-edition/videos/2021/01/mele-comparison-video-me1-og.webm",
    */
    '../videos/mass-effect-legendary-edition-first_before.mp4',
    '../videos/mass-effect-legendary-edition-first_before.webm'
];
video_before_list[1] = [
    /*
    "https://media.contentapi.ea.com/content/dam/eacom/mass-effect-legendary-edition/videos/2021/01/mele-comparison-video-me2-og.mp4",
    "https://media.contentapi.ea.com/content/dam/eacom/mass-effect-legendary-edition/videos/2021/01/mele-comparison-video-me2-og.webm"
    */
    '../videos/mass-effect-legendary-edition-second_before.mp4',
    '../videos/mass-effect-legendary-edition-second_before.webm'
];

function changeButtonColour(e) {
    var img_after = document.getElementById('comparison__frame').getElementsByClassName("figure")[0];
    var img_before = document.getElementById('divisor');
    var video_after = document.getElementById('video-after');
    var video_before = document.getElementById('video-before');
    var cur_btn = document.getElementById('btn-'+e)
    var url_address_after = "url('../img/game-comparison-"+e+"-after.jpg')";
    var url_address_before = "url('../img/game-comparison-"+e+"-before.jpg')";
    var howManyButtons = $(".comparison__button").length;
    for (i = 1; i <= howManyButtons; i++) {
        if (i !=e) {
            $('#btn-'+i).removeClass('active')
        }
    };
    $(cur_btn).addClass('active');
    img_before.style.backgroundImage = url_address_before;
    img_after.style.backgroundImage = url_address_after;

    if ([1, 3].indexOf(e) >= 0) {
        img_before.style.backgroundImage = "none";
        img_after.style.backgroundImage = "none";
        video_after.style.width = 100+'%';
        video_before.style.width = 100+'%';
        if (e == 1) {
            video_after.src = video_after_list[0][0]
            video_after.src = video_after_list[0][1]
            video_before.src = video_before_list[0][0]
            video_before.src = video_before_list[0][1]
        } else {
            video_after.src = video_after_list[1][0]
            video_after.src = video_after_list[1][1]
            video_before.src = video_before_list[1][0]
            video_before.src = video_before_list[1][1]
        };
    } else {
        video_after.src = "";
        video_before.src = "";
        video_after.style.width = 0+'%';
        // video_before.style.width = 0+'%';
    };
};

function moveDivisor() {
    const divisor = document.getElementById("divisor");
    const slider = document.getElementById("slider");
    const splitter = document.getElementById("comparison__splitter");
    var splitterWidth = $(splitter).width();
    var comparisonWidth = $('#comparison__frame').width();
    var splitterReplacment = +((splitterWidth*50/comparisonWidth).toFixed(2));
    divisor.style.width = slider.value+"%";
    splitter.style.left = slider.value-splitterReplacment+"%";
}

