function geoFindMe(L, map, csrf_token) {

    function success(position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        var icon = L.divIcon({
            className: 'custom-div-icon',
            html: "<div style='background-color:#c30b82;' class='marker-pin'></div><i class='fas fa-user'></i>",
            iconSize: [30, 42],
            iconAnchor: [15, 42]
        });

        L.marker([latitude, longitude], {
            icon: icon
        }).bindPopup('Votre position').addTo(map);

        data = {
            "latitude": latitude,
            "longitude": longitude,
            csrfmiddlewaretoken: csrf_token
        };
        $.ajax({
            type: "POST",
            url: "/current_coordinates",
            data: data,

            success: function (msg) {
                console.log('Succeeded!');
            }
        });
    }

    function error() {
        console.log('Unable to retrieve your location');
    }

    if (!navigator.geolocation) {
        console.log('Geolocation is not supported by your browser');
    } else {
        console.log('Locating…');
        navigator.geolocation.getCurrentPosition(success, error);
    }
}