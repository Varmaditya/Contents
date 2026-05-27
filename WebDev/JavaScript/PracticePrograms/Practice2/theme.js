function recommendTheme() {
    let mood = document.getElementById("mood").value;

    let result = mood === "calm" ? "🌙 Dark Blue Relaxation Theme" : 
                mood === "energetic" ? "🔥 Neon Red Energy Theme" : 
                        "📘 Minimal Focus Theme";

    document.getElementById("result").innerHTML = result;
}
