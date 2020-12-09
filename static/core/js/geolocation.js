function geoFindMe(L, map, csrf_token) {
    
    function success(position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        console.log(latitude, longitude);
        L.marker([latitude, longitude]).bindPopup('Votre position').addTo(map);

        data = {
            "latitude": latitude,
            "longitude": longitude,
            csrfmiddlewaretoken: csrf_token
        };
        console.log(data);
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