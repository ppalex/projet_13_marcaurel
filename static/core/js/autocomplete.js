$(function () {
    $("#city-search").autocomplete({
        source: '/autocomplete'
    });

});

export default (function add_auto_complete(element) {

    console.log(element);
    element.autocomplete({
        source: '/player-autocomplete'        

    });

});