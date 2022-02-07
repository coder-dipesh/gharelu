
$('.slider').slick({
	dots: true,
	infinite: true,
	speed: 300,
	slidesToShow: 3,
	slidesToScroll: 3,
	responsive: [{
		breakpoint: 1440,
		settings: {
		  slidesToShow: 3,
		  slidesToScroll: 3,
		  infinite: true,
		  dots: true
		},
	  },
	  {
		breakpoint: 1024,
		settings: {
		  slidesToShow: 1,
		  slidesToScroll: 1,
		  infinite: true,
		  dots: true
		},
	  },
	  {
		breakpoint: 600,
		settings: {
		  slidesToShow: 1,
		  slidesToScroll: 1
		}
	  },
	  {
		breakpoint: 480,
		settings: {
		  slidesToShow: 1,
		  slidesToScroll: 1
		}
	  }
	]
  });

//   var multipleCardCarousel = document.querySelector(
//   "#carouselExampleControls3");
// if (window.matchMedia("(min-width: 768px)").matches) {
//   var carousel = new bootstrap.Carousel(multipleCardCarousel, {
//     interval: false,
//   });
//   var carouselWidth = $(".carousel-inner")[0].scrollWidth;
//   var cardWidth = $(".carousel-item").width();
//   var scrollPosition = 0;
//   $("#carouselExampleControls3 .carousel-control-next").on("click", function () {
//     if (scrollPosition < carouselWidth - cardWidth * 4) {
//       scrollPosition += cardWidth;
//       $("#carouselExampleControls3 .carousel-inner").animate(
//         { scrollLeft: scrollPosition },
//         600
//       );
//     }
//   });
//   $("#carouselExampleControls3 .carousel-control-prev").on("click", function () {
//     if (scrollPosition > 0) {
//       scrollPosition -= cardWidth;
//       $("#carouselExampleControls3 .carousel-inner").animate(
//         { scrollLeft: scrollPosition },
//         600
//       );
//     }
//   });
// } else {
//   $(multipleCardCarousel).addClass("slide");
// }

// $(".hover").mouseleave(
// 	function () {
// 	  $(this).removeClass("hover");
// 	}
//   );
 