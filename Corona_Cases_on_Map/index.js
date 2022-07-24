function updateMap() {
    fetch("/data.json")
        .then(response => response.json())
        .then(rsp => {
            // console.log(rsp.data);
            console.log(`Updating map with realtime data`);
            rsp.data.forEach(element => {
                longitude = element.longitude;
                latitude = element.latitude;
                cases = element.infected;
                recovered = element.recovered;

                col = `rgb(${cases+50},0,0)`;
                col2 = `rgb(0,0,${recovered+50})`;
                
                //Mark on Map
                new mapboxgl.Marker({
                    // draggable: false,
                    color: col2
                })
                    .setLngLat([longitude, latitude])
                    .addTo(map);
            });
        })
}

// updateMap();
let interval = 20000;
setInterval(updateMap, interval);