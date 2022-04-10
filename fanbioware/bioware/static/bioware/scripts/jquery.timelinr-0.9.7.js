/* ----------------------------------
jQuery Timelinr 0.9.7
tested with jQuery v1.6+

Copyright 2011, CSSLab.cl
Free under the MIT license.
http://www.opensource.org/licenses/mit-license.php

instructions: http://www.csslab.cl/2011/08/18/jquery-timelinr/
---------------------------------- */

jQuery.fn.timelinr = function (options) {
    // default plugin settings
    settings = jQuery.extend({
        orientation: 'horizontal', // value: horizontal | vertical, default to horizontal
        wrapper: 'wrapper',
        containerDiv: '#timeline',  // value: any HTML tag or #id, default to #timeline
        datesDiv: '#dates',     // value: any HTML tag or #id, default to #dates
        datesSelectedClass: 'selected',   // value: any class, default to selected
        datesSpeed: 'normal',     // value: integer between 100 and 1000 (recommended) or 'slow', 'normal' or 'fast'; default to normal
        issuesDiv: '#issues',    // value: any HTML tag or #id, default to #issues
        issuesSelectedClass: 'selected',   // value: any class, default to selected
        issuesSpeed: 'fast',       // value: integer between 100 and 1000 (recommended) or 'slow', 'normal' or 'fast'; default to fast
        prevButton: '#prev',      // value: any HTML tag or #id, default to #prev
        nextButton: '#next',      // value: any HTML tag or #id, default to #next
        arrowKeys: 'false',      // value: true | false, default to false
        startAt: 2,            // value: integer, default to 1 (first)
        autoPlay: 'false',      // value: true | false, default to false
        autoPlayDirection: 'forward',    // value: forward | backward, default to forward
        autoPlayPause: 2000          // value: integer (1000 = 1 seg), default to 2000 (2segs)
    }, options);

    $(function () {
        // Checks if required elements exist on page before initializing timelinr | improvement since 0.9.55
        if ($(settings.datesDiv).length > 0 && $(settings.issuesDiv).length > 0) {
            // setting variables... many of them
            var howManyDates = $(settings.datesDiv + ' li').length;
            var howManyIssues = $(settings.issuesDiv + ' li').length;

            // set positions!
            wrapper = document.getElementsByClassName("wrapper")[0];
            widthWrapper = $(wrapper).width();
            if (window.screen.width < 640) {
                $(settings.datesDiv).width(window.screen.width / 3 * howManyDates + 60);
            } else {
                $(settings.datesDiv).width(widthWrapper / 3 * howManyDates);
            };
            //$(settings.datesDiv).width(widthWrapper / 3 * howManyDates);
            $(settings.issuesDiv).width(widthWrapper * howManyDates);
            var widthIssue = $(settings.issuesDiv + ' li').width();
            var widthDate = $(settings.datesDiv + ' li').width();
            if (window.screen.width < 640) {
                $(settings.datesDiv).css('marginLeft', widthDate - 33);
            } else {
                $(settings.datesDiv).css('marginLeft', widthDate);
            };
            var defaultPositionDates = parseInt($(settings.datesDiv).css('marginLeft').substring(0, $(settings.datesDiv).css('marginLeft').indexOf('px')));

            // Touch features
            var posX1 = 0,
                posX2 = 0,
                posY1 = 0,
                posY2 = 0,
                posInitial = '',
                posFinal = '',
                threshold = 100,
                isSwipe = false,
                isScroll = false,
                allowSwipe = true,
                started = false;
                slider = document.getElementById('issues');

            slider.onmousedown = dragStart;
            slider.addEventListener('touchstart', dragStart, false);
            slider.addEventListener('touchmove', dragAction, false);
            slider.addEventListener('touchend', dragEnd, false);

            function dragStart (e) {
                e = e || window.event;
                posInitial = slider.offsetLeft;
                if (e.type == 'touchstart') {
                    posX1 = e.touches[0].clientX;
                    posY1 = e.touches[0].clientY;
                } else {
                    posX1 = e.clientX;
                    posY1 = e.clientY;
                    document.onmouseup = dragEnd;
                    document.onmousemove = dragAction;
                }
            }

            function dragAction (e) {
                e = e || window.event;
                if (e.type == 'touchmove') {
                    posX2 = posX1 - e.touches[0].clientX;
                    posX1 = e.touches[0].clientX;
                    posY2 = posY1 - e.touches[0].clientY;
                    posY1 = e.touches[0].clientY;
                } else {
                    posX2 = posX1 - e.clientX;
                    posX1 = e.clientX;
                }
                if (!isSwipe && !isScroll) {
                    let posY = Math.abs(posY2);
                    if (posY > 7 || posX2 === 0) {
                        isScroll = true;
                        allowSwipe = false;
                        isSwipe = false;
                    } else if (posY < 7) {
                        e.preventDefault();
                        isSwipe = true;
                    }
                };
                if (isSwipe) {
                    slider.style.marginLeft = (slider.offsetLeft - posX2) + "px";
                }
            };

            function dragEnd (e) {
                posFinal = slider.offsetLeft;
                if (posFinal - posInitial < -threshold) {
                    $(settings.nextButton).click();
                } else if (posFinal - posInitial > threshold) {
                    $(settings.prevButton).click();
                } else {
                    slider.style.marginLeft = (posInitial) + "px";
                }

                document.onmouseup = null;
                document.onmousemove = null;
            }

            //Date click function
            $(settings.datesDiv + ' a').click(function (event) {
                event.preventDefault();
                // first vars
                var currentIndex = $(this).parent().prevAll().length;

                // Resize function
                $(window).resize(function () {
                    document.location.reload();
                });
                // moving the elements
                $(settings.issuesDiv).animate({ 'marginLeft': -widthIssue * currentIndex }, { queue: false, duration: settings.issuesSpeed });
                $(settings.issuesDiv + ' li').removeClass(settings.issuesSelectedClass).eq(currentIndex).addClass(settings.issuesSelectedClass);
                var issueHeight = ($(settings.issuesDiv + ' li.selected').height());
                $(settings.issuesDiv).height(issueHeight);
                // prev/next buttons now disappears on first/last issue | bugfix from 0.9.51: lower than 1 issue hide the arrows | bugfixed: arrows not showing when jumping from first to last date
                let prev = document.querySelector("#prev");
                if ($(settings.issuesDiv + ' li:first-child').hasClass(settings.issuesSelectedClass)) {
                    prev.style.backgroundImage = "url('./img/svg/timeline-prev-deactive-arrow.svg')";
                } else {
                    prev.style.backgroundImage = "url('./img/svg/timeline-prev-arrow.svg')"
                }
                let next = document.querySelector("#next");
                if ($(settings.issuesDiv + ' li:last-child').hasClass(settings.issuesSelectedClass)) {
                    next.style.backgroundImage = "url('./img/svg/timeline-next-deactive-arrow.svg')";
                } else {
                    next.style.backgroundImage = "url('./img/svg/timeline-next-arrow.svg')"
                }
                // change timeline-line on first/last issue

                // now moving the dates
                $(settings.datesDiv + ' a').removeClass(settings.datesSelectedClass);
                $(settings.datesDiv + ' li').removeClass('current_date');
                $(this).addClass(settings.datesSelectedClass);
                $(settings.datesDiv + ' li').eq(currentIndex).removeClass('prev_date').removeClass('next_date').addClass('current_date');
                for (let i = 0; i < currentIndex; i ++) {
                    $(settings.datesDiv + ' li').eq(i).addClass('prev_date');
                };
                for (let i = currentIndex + 1; i <= howManyDates; i ++) {
                    $(settings.datesDiv + ' li').eq(i).addClass('next_date');
                };
                $(settings.datesDiv).animate({ 'marginLeft': defaultPositionDates - (widthDate * currentIndex) }, { queue: false, duration: 'settings.datesSpeed' });
            });
            $(settings.nextButton).bind('click', function (event) {
                event.preventDefault();
                // bugixed from 0.9.54: now the dates gets centered when there's too much dates.
                var currentIndex = $(settings.issuesDiv).find('li.' + settings.issuesSelectedClass).index();
                var currentPositionIssues = parseInt($(settings.issuesDiv).css('marginLeft').substring(0, $(settings.issuesDiv).css('marginLeft').indexOf('px')));
                var currentPositionDates = parseInt($(settings.datesDiv).css('marginLeft').substring(0, $(settings.datesDiv).css('marginLeft').indexOf('px')));
                if (currentPositionIssues <= -(widthIssue * howManyIssues - (widthIssue))) {
                    $(settings.issuesDiv).stop();
                    $(settings.datesDiv + ' li:last-child a').click();
                } else {
                    if (!$(settings.issuesDiv).is(':animated')) {
                        // bugixed from 0.9.52: now the dates gets centered when there's too much dates.
                        $(settings.datesDiv + ' li').eq(currentIndex + 1).find('a').trigger('click');
                    }
                };
                let next = document.querySelector("#next");
                if ($(settings.issuesDiv + ' li:last-child').hasClass(settings.issuesSelectedClass)) {
                    next.style.backgroundImage = "url('./img/svg/timeline-next-deactive-arrow.svg')";
                } else {
                    next.style.backgroundImage = "url('./img/svg/timeline-next-arrow.svg')"
                }
            });

            $(settings.prevButton).click(function (event) {
                event.preventDefault();
                // bugixed from 0.9.54: now the dates gets centered when there's too much dates.
                var currentIndex = $(settings.issuesDiv).find('li.' + settings.issuesSelectedClass).index();
                var currentPositionIssues = parseInt($(settings.issuesDiv).css('marginLeft').substring(0, $(settings.issuesDiv).css('marginLeft').indexOf('px')));
                var currentIssueIndex = currentPositionIssues / widthIssue;
                var currentPositionDates = parseInt($(settings.datesDiv).css('marginLeft').substring(0, $(settings.datesDiv).css('marginLeft').indexOf('px')));
                var currentIssueDate = currentPositionDates + widthDate;
                if (currentPositionIssues >= 0) {
                    $(settings.issuesDiv).stop();
                    $(settings.datesDiv + ' li:first-child a').click();
                } else {
                    if (!$(settings.issuesDiv).is(':animated')) {
                        // bugixed from 0.9.54: now the dates gets centered when there's too much dates.
                        $(settings.datesDiv + ' li').eq(currentIndex - 1).find('a').trigger('click');
                    }
                };
                // prev/next buttons now disappears on first/last issue | bugfix from 0.9.51: lower than 1 issue hide the arrows
                let prev = document.querySelector("#prev");
                if ($(settings.issuesDiv + ' li:first-child').hasClass(settings.issuesSelectedClass)) {
                    prev.style.backgroundImage = "url('./img/svg/timeline-prev-deactive-arrow.svg')";
                } else {
                    prev.style.backgroundImage = "url('./img/svg/timeline-prev-arrow.svg')"
                }
            });
            // keyboard navigation, added since 0.9.1
            if (settings.arrowKeys == 'true') {
                $(document).keydown(function (event) {
                    if (event.keyCode == 39) {
                        $(settings.nextButton).click();
                    }
                    if (event.keyCode == 37) {
                        $(settings.prevButton).click();
                    }
                });
            }
            // default position startAt, added since 0.9.3
            $(settings.datesDiv + ' li').eq(settings.startAt - 1).addClass('current_date').find('a').trigger('click');
            $(settings.datesDiv + ' li').eq(settings.startAt - 2).addClass('prev_date');
            $(settings.datesDiv + ' li').eq(settings.startAt).addClass('next_date');
            // autoPlay, added since 0.9.4
            if (settings.autoPlay == 'true') {
                // set default timer
                var timer = setInterval(autoPlay, settings.autoPlayPause);
                // pause autoplay on hover
                $(settings.containerDiv).hover(function (ev) {
                    clearInterval(timer);
                }, function (ev) {
                    // start again timer on mouse out
                    timer = setInterval(autoPlay, settings.autoPlayPause);
                });
            }
        }
    });
}

// autoPlay, added since 0.9.4
function autoPlay() {
    var currentDate = $(settings.datesDiv).find('a.' + settings.datesSelectedClass);
    if (settings.autoPlayDirection == 'forward') {
        if (currentDate.parent().is('li:last-child')) {
            $(settings.datesDiv + ' li:first-child').find('a').trigger('click');
        } else {
            currentDate.parent().next().find('a').trigger('click');
        }
    } else if (settings.autoPlayDirection == 'backward') {
        if (currentDate.parent().is('li:first-child')) {
            $(settings.datesDiv + ' li:last-child').find('a').trigger('click');
        } else {
            currentDate.parent().prev().find('a').trigger('click');
        }
    }
}
