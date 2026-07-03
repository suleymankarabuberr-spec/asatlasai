async function send(){

const text=document.getElementById("message").value;

const res=await fetch("/chat",{

method:"POST"

});

const data=await res.json();

document.getElementById("messages").innerHTML+=

"<p><b>Sen:</b> "+text+"</p>";

document.getElementById("messages").innerHTML+=

"<p><b>asATLASAI:</b> "+data.response+"</p>";

}
async function send() {
    const input = document.getElementById("message");
    const messages = document.getElementById("messages");

    const text = input.value;
    if (!text) return;

    messages.innerHTML += `<div><b>Sen:</b> ${text}</div>`;

    const res = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: text })
    });

    const data = await res.json();

    messages.innerHTML += `<div><b>asATLASAI:</b> ${data.response}</div>`;

    input.value = "";
}
