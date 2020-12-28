## coding: utf-8
<!DOCTYPE html>
<html>
   <head>
      <title>Web-Teams</title>
      <meta charset="UTF-8" />
      <link rel="preconnect" href="https://fonts.gstatic.com" />
      <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;800&family=Quicksand:wght@400;700&display=swap" rel="stylesheet" />
      <link href="/webteams.css" rel="stylesheet" type="text/css" />
   </head>
   <body>
      <div class="outer-flex-container">
         <form id="form" action="/save" method="POST">
            <input type="hidden" value="${key}" id="id_param" name="id_param" />
            <div>
               <label for="name1">1. Name</label>
               <input type="text"
                      value="${data[0]}"
                      id="name1"
                      name="name1" required />
            </div>
            <div>
               <label for="vorname1">1. Vorname</label>
               <input type="text"
                      value="${data[1]}"
                      id="vorname1"
                      name="vorname1" required />
            </div>
            <div>
               <label for="matrnr1">1. Matrikelnummer</label>
               <input type="number"
                      value="${data[2]}"
                      id="matrnr1"
                      name="matrnr1" required />
            </div>
            <div>
               <label for="semesteranzahl1">1. Semesteranzahl</label>
               <input type="number"
                      value="${data[3]}"
                      id="semesteranzahl1"
                      name="semesteranzahl1" required />
            </div>
            <div>
               <label for="name2">2. Name</label>
               <input type="text"
                      value="${data[4]}"
                      id="name2"
                      name="name2" required />
            </div>
            <div>
               <label for="vorname2">2. Vorname</label>
               <input type="text"
                      value="${data[5]}"
                      id="vorname2"
                      name="vorname2" required />
            </div>
            <div>
               <label for="matrnr2">2. Matrikelnummer</label>
               <input type="number"
                      value="${data[6]}"
                      id="matrnr2"
                      name="matrnr2" required />
            </div>
            <div>
               <label for="semesteranzahl2">2. Semesteranzahl</label>
               <input type="number"
                      value="${data[7]}"
                      id="semesteranzahl2"
                      name="semesteranzahl2" required />
            </div>
            <div class="inner-flex-container">
               <input type="submit" value="speichern" class="pseudo-button"/>
               <a class="pseudo-button" href="/">abbrechen</a>
            </div>
         </form>
      </div>
      <script type="text/javascript" src="/webteams.js"></script>
   </body>
</html>