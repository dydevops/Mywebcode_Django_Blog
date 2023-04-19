let previews = document.getElementsByClassName('preview');
Array.from(previews).forEach((element)=>{
  element.innerHTML = element.innerText;
})

setTimeout(function(){
  $('#message').fadeOut('slow')
}, 4000)

function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
function dkrrt() {
  var x = document.getElementById("dkinput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}