## coding: utf-8
<!DOCTYPE html>
<html>
    <head>
        <title>Mitarbeiterqualifikation</title>
        <meta charset="UTF-8" />
        <link rel="preconnect" href="https://fonts.gstatic.com" />
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;800&family=Quicksand:wght@400;700&display=swap" rel="stylesheet" />
        <link href="/mq.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <div class="head-flex-container">
            <span class="left-flex-row">
                <h1>Mitarbeiterqualifikation</h1>
                <h1>Version 1.0 / 28.12.2020</h1>
            </span>
            <span class="right-flex-row">
                <h1>Marina Inokuchi, Matr.-Nr. 1287686</h1>
            </span>
        </div>
        <div class="body-flex-container">
            <span class="sidebar-flex-container left-flex-row">
                <div class="menu-item menu-1">
                    <a href="/">Startseite</a>
                </div>
                <div class="menu-item menu-2">
                    <a href="/list_employees">Pflege Mitarbeiterdaten</a>
                    <a href="/list_trainings">Pflege Weiterbildungen</a>
                </div>
                <div class="menu-item menu-3">
                    <h2>Teilnahme</h2>
                    <li><a href="/participation_employees">Sichtweise Mitarbeiter</a></li>
                    <li><a href="/participation_trainings">Sichtweise Weiterbildungen</a></li>
                </div>
                <div class="menu-item menu-4">
                    <h2>Auswertungen</h2>
                    <li><a href="https://www.google.com/">Mitarbeiter</a></li>
                    <li><a href="https://www.google.com/">Weiterbildungen</a></li>
                    <li><a href="https://www.google.com/">Zertifikate</a></li>
                </div>
            </span>
            <span class="content-flex-container right-flex-row">
                <div class="content">
                    ${self.body()}
                </div>
            </span>
        </div>
        <script type="text/javascript" src="/mq.js"></script>
    </body>
</html>