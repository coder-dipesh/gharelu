
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

// $(".hover").mouseleave(
// 	function () {
// 	  $(this).removeClass("hover");
// 	}
//   );
  

