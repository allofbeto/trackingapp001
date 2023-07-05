$(document).ready(function() {
  $('.blob-button').click(function() {
    $(this).find('.bar').toggleClass('bar-active');
    $(this).siblings('.link').toggleClass('active');
  });

  $('.blob-button').click(function() {
    $(this).addClass('blob-button-active');
    $(this).on('transitionend', function() {
      $(this).removeClass('button-active');
    });
  });
});