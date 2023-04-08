/*
 Template Name: 
 File Name: custom.js
 Author Name: ThemeVault
 Author URI: http://www.themevault.net/
 License URI: http://www.themevault.net/license/
 */


$(document).ready(function () {

    var $window = $(window),
            $body = $('body'),
            $wrapper = $('#wrapper'),
            $header = $('#header'),
            $banner = $('#banner');


    $('.tv-scroll').scrolly({
        offset: function () {
            return $header.height() - 2;
        }
    });
    // Header.
    if ($banner.length > 0
            && $header.hasClass('alt')) {

        $window.on('resize', function () {
            $window.trigger('scroll');
        });

        $window.on('load', function () {

            $banner.scrollex({
                bottom: $header.height() + 10,
                terminate: function () {
                    $header.removeClass('alt');
                },
                enter: function () {
                    $header.addClass('alt');
                },
                leave: function () {
                    $header.removeClass('alt');
                    $header.addClass('reveal');
                }
            });

            window.setTimeout(function () {
                $window.triggerHandler('scroll');
            }, 100);

        });
    }
    $(".slide-wrapper").slick({
        dots: false,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        autoplaySpeed: 5000,
        autoplay: true,
        arrow: false
    });
});
