jQuery(function () {
  jQuery('DIV#toggle_header').click(toggleColor);
});

function toggleColor () {
  if (jQuery('header').hasClass('green')) {
    jQuery('header').removeClass('green').addClass('red');
  } else {
    jQuery('header').removeClass('red').addClass('green');
  }
}
