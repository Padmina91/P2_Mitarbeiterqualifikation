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
         <table>
            <tr class="team-header">
               <th>Name</th><th>Vorname</th><th>Matr.-Nr.</th><th>Semesterzahl</th>
            </tr>
            % for key in data:
            <tr class="team">
               <tr>
                  <td>${data[key][0]}</td>
                  <td>${data[key][1]}</td>
                  <td>${data[key][2]}</td>
                  <td>${data[key][3]}</td>
               </tr>
               <tr>
                  <td>${data[key][4]}</td>
                  <td>${data[key][5]}</td>
                  <td>${data[key][6]}</td>
                  <td>${data[key][7]}</td>
                  <td><a class="pseudo-button" href="/edit/${key}">bearbeiten</a></td>
                  <td><a class="pseudo-button delete-button" href="/delete/${key}">löschen</a></td>
               </tr>
            </tr>
            % endfor
         </table>
         <div class="inner-flex-container">
            <span>
               <a class="pseudo-button" href="/add">erfassen</a>
            </span>
            <span>
               <a class="pseudo-button" href="/toggle_view">als Aufzählung darstellen</a>
            </span>
         </div>
      </div>
      <script type="text/javascript" src="/webteams.js"></script>
   </body>
</html>