const project_button = document.getElementById("project");
const project_modal = document.getElementById("projectModal");
const result_button = document.getElementById("result");
const result_modal = document.getElementById("resultModal");


project_button.onclick = function(){
  projectModal.style.display = "block";
}

result_button.onclick = function(){
  result_modal.style.display = "block";
}

window.onclick = function(event){
  if (event.target == project_modal) {
    projectModal.style.display = "none";
  }
  else if (event.target == result_modal) {
    result_modal.style.display = "none";
  }
}
