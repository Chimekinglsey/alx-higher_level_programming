jQuery(function () {
  jQuery('DIV#add_item').click(addItem);
});

function addItem () {
  jQuery('UL.my_list').append('<li>Item</li>');
}
