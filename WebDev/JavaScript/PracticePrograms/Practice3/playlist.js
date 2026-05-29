function generatePlaylist() {
    let songs = "";
    let count = 1;

    while (count <= 5) {
        songs += "<div class='item'>" + "🎵 Playing Song " + count + "</div>";
        count++;
    }

    document.getElementById("output").innerHTML = songs;
}
