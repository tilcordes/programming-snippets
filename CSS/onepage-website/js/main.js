$(document).ready(function() {
    $('.burger').click(function() {
        $('.nav_links').toggleClass('active');
    });
    $('a[href*="#"]').click(function(){
        var finish = $(this.hash);
        if(finish.length){
          var distance_top = finish.offset().top;
          $('html,body').animate({scrollTop: distance_top},750);
        return false;
      }
      });	
});