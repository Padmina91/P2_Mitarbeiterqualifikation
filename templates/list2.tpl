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
         <%
            nr = 0
         %>
         <ul>
            % for key in data:
            <%
               nr += 1
            %>
            <li><span class="team-header">Team ${nr}:</span>
               <a class="pseudo-button" href="/edit/${key}">bearbeiten</a>
               <a class="pseudo-button delete-button" href="/delete/${key}">löschen</a>
               <ul>
                  <li>Name: ${data[key][0]}, Vorname: ${data[key][1]}, Matr-Nr.: ${data[key][2]}, Anzahl Semester: ${data[key][3]}</li>
                  <li>Name: ${data[key][4]}, Vorname: ${data[key][5]}, Matr-Nr.: ${data[key][6]}, Anzahl Semester: ${data[key][7]}</li>
               </ul>
            </li>
            % endfor
         </ul>
         <div class="inner-flex-container">
            <span>
               <a class="pseudo-button" href="/add">erfassen</a>
            </span>
            <span>
               <a class="pseudo-button" href="/toggle_view">als Liste darstellen</a>
            </span>
         </div>
      </div>
      <script type="text/javascript" src="/webteams.js"></script>
   </body>
</html>