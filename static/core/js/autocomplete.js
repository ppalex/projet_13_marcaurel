$(function () {
    $("#city-search").autocomplete({
        source: '/autocomplete'
    });
    
});

$(function () {
    $("#player-search").autocomplete({
        source: '/player-autocomplete',
        
    });
    
});