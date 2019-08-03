var nightModeOn = false;

function nightMode() {
    map = new google.maps.Map(
    document.getElementById("map_canvas"), 
    {
        center: {lat: userPos[0], lng: userPos[1]},
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        styles: [
            {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
            {
              featureType: 'administrative.locality',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'poi',
              elementType: 'labels.text.fill',
              stylers: [{visibility: 'off'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'geometry',
              stylers: [{color: '#263c3f'}]
            },
            {
              featureType: 'poi.business',
              stylers: [{visibility: 'off'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'labels.text.fill',
              stylers: [{color: '#6b9a76'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry',
              stylers: [{color: '#38414e'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry.stroke',
              stylers: [{color: '#212a37'}]
            },
            {
              featureType: 'road',
              elementType: 'labels.text.fill',
              stylers: [{color: '#9ca5b3'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry',
              stylers: [{color: '#746855'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry.stroke',
              stylers: [{color: '#1f2835'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'labels.text.fill',
              stylers: [{color: '#f3d19c'}]
            },
            {
              featureType: 'transit',
              stylers: [{visibility: 'off'}]
            },
            {
              featureType: 'transit.station',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'water',
              elementType: 'geometry',
              stylers: [{color: '#17263c'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.fill',
              stylers: [{color: '#515c6d'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.stroke',
              stylers: [{color: '#17263c'}]
            }
        ]
    });
}

function dayMode() {

    map = new google.maps.Map(
    
    document.getElementById("map_canvas"), 
    {
        center: {lat: userPos[0], lng: userPos[1]},
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        styles: [
          {
            "featureType": "poi",
            "elementType": "labels.text",
            "stylers": [
              {
                "visibility": "off"
              }
            ]
          },
          {
            "featureType": "poi.business",
            "stylers": [
              {
                "visibility": "off"
              }
            ]
          },
          {
            "featureType": "road",
            "elementType": "labels.icon",
            "stylers": [
              {
                "visibility": "off"
              }
            ]
          },
          {
            "featureType": "transit",
            "stylers": [
              {
                "visibility": "off"
              }
            ]
          }
        ]
    });
}

var routeOpen = false;

function openRoute(element){
  
  if(routeOpen)
    return;
  childrenList = $("#rightPanel").children();
  
  var eleNumber = element.id.split('e')[1];
  for (var i = 1; i <= childrenList.length; i++) {
    if(i == eleNumber){
      continue;
    }
    else{
      $(childrenList[i-1]).fadeOut("slow");  
      $(childrenList[i-1]).hide();
    }
  }

  $($(element).children()[3]).fadeIn("fast");

  for (var j = 0; j < hardData[eleNumber-1].R.length; j++) {
    mapFun(hardData[eleNumber-1].R[j], hardData[eleNumber-1].M[j]); 
  }
  map.setZoom(10);
  routeOpen = true;
}

function closeRoute(element){
  
  if(!routeOpen)
    return;
  childrenList = $("#rightPanel").children();

  var eleNumber = $($(element).parent()).attr('id').split('e')[1];
  
  for (var i = 1; i <= childrenList.length; i++) {
    if(i == eleNumber){
      continue;
    }
    else{
      $(childrenList[i-1]).fadeIn("slow");  
      $(childrenList[i-1]).show();
    }
  }

  $(element).fadeOut("fast");

  for (var j = 0; j < curPolyline.length; j++) {
    curPolyline[j].setMap(null);
  }

  setTimeout(() => {
    routeOpen = false;
  }, 1000)

}

function toggleNightModeShift(){
  if(!nightModeOn){
    nightMode(); 
    $("#nightModeRadio").addClass("bg-success");
    $("#nightModeRadio").removeClass("bg-danger");
    $("#nightModeRadio").text("ON");
  }
  else{
    dayMode();
    $("#nightModeRadio").removeClass("bg-success");
    $("#nightModeRadio").addClass("bg-danger");
    $("#nightModeRadio").text("OFF");
  }
  nightModeOn = !nightModeOn;
  resetSite();
}

function populateData(data){
  for (var i = 0; i < data.length; i++) {
    h = parseInt((data[i].T/60)/60);
    m = parseInt((data[i].T/60)%60);
    timePlace = h+"h"+m+"m";
    var s = "<p class='m-0 mb-2 lead font-weight-bold text-primary'>Checkpoints</p>";
    for(var k = 0; k < data[i].I.length; k++){
      s += '<p class="m-0 mb-2 small">' + String(k+1) + '. ' + data[i].I[k] + '</p>'
    }
    if(data[i].M.includes("Walk")){
      s += "<p class='m-0 mb-2 mt-4 lead font-weight-bold text-danger'>Caution</p>" + "<p class='m-0 small'><i>The pollution levels in the region you're travelling through is experiencing high levels of pollution. Please make sure to have a N95 mask on hand while walking on this trip.</i></p>";
    }
    domELe = '<div class="routePanel row m-1 py-2 mb-4" id="route' + (i+1) +'" onclick="openRoute(this);"><div class="col-6 p-0 pl-3 text-left"><img src="./src/images/modes/uber.png" alt="Uber" class="minify-icons" id="uber"><img src="./src/images/modes/bus.png" alt="Bus" class="minify-icons" id="bus"><img src="./src/images/modes/walking.png" alt="Walk" class="minify-icons" id="walk"><img src="./src/images/modes/metro.png" alt="Metro" class="minify-icons" id="metro"></div><div class="routeText col-3 p-0"><span style="position: absolute; top: 50%; left: 50%; transform: translateX(-50%) translateY(-50%);" id="price">₹' + data[i].P + '</span></div><div class="routeText2 col-3 text-dark small p-0"><span style="position: absolute; top: 50%; left: 50%; transform: translateX(-50%) translateY(-50%);" id="time">' + timePlace + '</span></div><div class="col-12 pt-2 pb-3 text-left" id="routeData" onclick="closeRoute(this);"> ' + s + '</div></div>';
    $("#rightPanel").append(domELe);
    if(!data[i].M.includes("Car")){
      $("#route" + (i+1)).find("#uber").hide();  
    }
    if(!data[i].M.includes("Walk")){
      $("#route" + (i+1)).find("#walk").hide();  
    }
    if(!data[i].M.includes("Bus")){
      $("#route" + (i+1)).find("#bus").hide();  
    }
    if(!data[i].M.includes("Metro")){
      $("#route" + (i+1)).find("#metro").hide();  
    }
  }
}

var curPolyline = [];

function mapFun(points, mVal){

  var color = '#DDD92A';

  if(mVal == "Car"){
    color = '#36558F';
  }
  else if(mVal == "Bus"){
    color = '#53599A';
  }
  else if(mVal == "Metro"){
    color = '#D63230';
  }
  else if(mVal == "Walk"){
    color = '#21897E';
  }

  var bounds = new google.maps.LatLngBounds();
  
  var path = google.maps.geometry.encoding.decodePath(points);
  
  for (var i = 0; i < path.length; i++) {
    bounds.extend(path[i]);
  }
  
  var polyline = new google.maps.Polyline({
    path: path,
    strokeColor: color,
    strokeOpacity: 0.8,
    strokeWeight: 8,
    fillColor: color,
    fillOpacity: 0.35,
    map: map
    // strokeColor: "#0000FF",
    // strokeOpacity: 1.0,
    // strokeWeight: 2
  });
  curPolyline.push(polyline);
  polyline.setMap(map);
  map.fitBounds(bounds);  
}
