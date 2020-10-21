// function for owl carousel
$('.owl-carousel').owlCarousel({
    //tells carousel to loop through items
    loop:true,
    //sets time delay for each item
    margin:10,
    nav:true,
    //tells carousel how many items to display on different device sizes
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
});

