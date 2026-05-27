function checkSubscription() {
    let plan = document.getElementById("plan").value;

    if (plan === "premium") {
        document.getElementById("result").innerHTML =
            "🎥 4K Streaming Enabled<br>" +
            "📺 Unlimited Access<br>" +
            "👥 Multiple Devices Supported";
    } else if (plan === "basic") {
        document.getElementById("result").innerHTML =
            "🎬 HD Streaming Enabled<br>" + "📱 Limited Devices";
    } else {
        document.getElementById("result").innerHTML =
            "⚠ Ads Enabled<br>" + "🔒 Premium Features Locked";
    }
}
