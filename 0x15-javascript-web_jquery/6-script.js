jQuery(function () {
  jQuery('DIV#update_header').click(updateHeader);
});
function updateHeader () {
  jQuery('header').text('New Header!!!');
}
