$(function() {
    $('a[href*="#"]').stop().click(function(){
        var finish = $(this.hash);
        if(finish.length){
          var distance_top = finish.offset().top;
          $('html,body').animate({scrollTop: distance_top},1000);
        return false;
      }
      });	
});