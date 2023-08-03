jQuery(function () {
  jQuery('DIV#red_header').click(changer());
});
jQuery(function changer () {
  jQuery('header').css('color', '#FF0000');
});
