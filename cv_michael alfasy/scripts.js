document.addEventListener('DOMContentLoaded', function() {
// When the event DOMContentLoaded occurs, it is safe to access the DOM

    // When the user scrolls the page, execute stickyNav and scrollFunction functions     
    window.addEventListener('scroll', stickyNav);
    window.addEventListener('scroll', scrollFunction);
   
    // Get the navbar
    var navbar = document.getElementById("navbar");

    // Get the offset position of the navbar
    var sticky = navbar.offsetTop;

    // Get the button
    var mybutton = document.getElementById("top");
    mybutton.addEventListener("click", topFunction); // When The User click this button execute the topFunction

    // Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
    function stickyNav() {
    if (window.pageYOffset > sticky) {
        navbar.classList.add("sticky")
    } else {
        navbar.classList.remove("sticky");
      }  
    }

    function scrollFunction() { 
        if (document.body.scrollTop > 25 || document.documentElement.scrollTop > 25) {
            mybutton.style.display = "block"; // show the block button
        } 
        else {
            mybutton.style.display = "none";  // hide the block button
        }
    }

    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }

})