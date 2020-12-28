"use strict"

document.addEventListener("DOMContentLoaded", () => {
   const delete_buttons = document.getElementsByClassName("delete-button");
   for (let delete_button of delete_buttons) {
      delete_button.addEventListener('click', function(event) {
         let delete_decision = confirm("Wollen Sie den Eintrag wirklich löschen?");
         if (!delete_decision) {
            event.preventDefault();
         }
      }, false);
   }
});