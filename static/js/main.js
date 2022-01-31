// (function () {
//   "use strict";
//   var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
//   tooltipTriggerList.forEach(function (tooltipTriggerEl) {
//     new bootstrap.Tooltip(tooltipTriggerEl);
//   });
// })();

// $(document).ready(function () {
//   $("#sidebarCollapse").on("click", function () {
//     $("#sidebar").toggleClass("active");
//   });
// });

// $(document).ready(() => {
//   let navText = ["<i class='bx bx-chevron-left'></i>", "<i class='bx bx-chevron-right'></i>"];
//   $("#hero-carousel").owlCarousel({
//     items: 1,
//     dots: false,
//     loop: true,
//     nav: true,
//     navText: navText,
//     autoplay: true,
//     autoplayHoverPause: true,
//   });
// });

// // Data Picker Initialization
// $(".datepicker").pickadate();

// ----------------Go to top button ------------------

//Get the button
const mybutton = document.getElementById("btn-back-to-top");

console.log(mybutton);

const refreshButtonVisibility = () => {
  if (document.documentElement.scrollTop <= 150) {
    mybutton.style.display = "none";
  } else {
    mybutton.style.display = "block";
  }
};
refreshButtonVisibility();

mybutton.addEventListener("click", () => {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
});

mybutton.addEventListener("scroll", (e) => {
  refreshButtonVisibility();
});

// $(window).on("scroll", function () {
//   var height = $(window).scrollTop();
//   if (height > 100) {
//     $("#btn-back-to-top").fadeIn();
//   } else {
//     $("#btn-back-to-top").fadeOut();
//   }
// });

// $("#btn-back-to-top").on("click", function (event) {
//   event.preventDefault();
//   $("html, body").animate({ scrollTop: 0 }, "slow");
//   return false;
// });
