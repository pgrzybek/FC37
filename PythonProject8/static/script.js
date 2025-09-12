
function handleClick() {
    let name = document.getElementById("username").value;

    fetch("/", {  // fetch wysyła POST właśnie na "/"
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerHTML = data.message;
        });
}

window.onload = function() {
    document.getElementById("sendBtn").addEventListener("click", handleClick);
};