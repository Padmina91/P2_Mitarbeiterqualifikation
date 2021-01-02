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

   const submit_buttons = document.getElementsByClassName("submit-button");
   const training_form = document.getElementById("training-form");
   for (let submit_button of submit_buttons) {
      submit_button.addEventListener('click', function(event) {
         training_form.submit();
         event.preventDefault();
      }, false);
   }

   const cancel_registration_buttons = document.getElementsByClassName("cancel-training");
   for (let cancel_registration_button of cancel_registration_buttons) {
      cancel_registration_button.addEventListener('click', function(event) {
         let cancel_registration_decision = confirm("Wollen Sie diese Teilnahme wirklich stornieren?");
         if (!cancel_registration_decision) {
            event.preventDefault();
         }
      }, false);
   }

   const cancel_participation_buttons = document.getElementsByClassName("cancel-participation");
   for (let cancel_participation_button of cancel_participation_buttons) {
      cancel_participation_button.addEventListener('click', function(event) {
         let cancel_participation_decision = confirm("Wollen Sie diese Weiterbildung wirklich abbrechen?");
         if (!cancel_participation_decision) {
            event.preventDefault();
         }
      }, false);
   }
});