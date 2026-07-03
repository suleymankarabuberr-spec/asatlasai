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
