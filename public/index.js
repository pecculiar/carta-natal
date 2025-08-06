function initAutocomplete() {
  const input = document.getElementById("city");
  const autocomplete = new google.maps.places.Autocomplete(input);

  autocomplete.addListener("place_changed", function () {
    const place = autocomplete.getPlace();
    if (place.geometry) {
      const lat = place.geometry.location.lat();
      const lng = place.geometry.location.lng();
      document.getElementById("lat").value = lat.toFixed(4);
      document.getElementById("lon").value = lng.toFixed(4);
    }
  });
}