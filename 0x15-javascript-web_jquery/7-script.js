jQuery(function () {
  jQuery.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    jQuery('DIV#character').text(data.name);
  });
});
