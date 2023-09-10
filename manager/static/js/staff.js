const create_button = document.getElementById("create");
const create_modal = document.getElementById("createModal");
const upload_button = document.getElementById("upload");
const upload_modal = document.getElementById("uploadModal");

create_button.onclick = function(){
  createModal.style.display = "block";
}

upload_button.onclick = function(){
  uploadModal.style.display = "block";
}

window.onclick = function(event){
  if (event.target == create_modal) {
    create_modal.style.display = "none";
  }
  else if (event.target == upload_modal) {
    upload_modal.style.display = "none";
  }
}
