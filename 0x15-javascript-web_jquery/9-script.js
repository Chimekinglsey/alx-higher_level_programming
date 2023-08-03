jQuery(function () {
  jQuery.get('https://hellosalut.stefanbohacek.dev/?lang=fr'
    , function (data) {
      jQuery('DIV#hello').text(data.hello);
    });
});
