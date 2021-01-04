## coding: utf-8
<!DOCTYPE html>
<html lang="de">
    <head>
        <title>Mitarbeiterqualifikation</title>
        <meta charset="UTF-8" />
        <link rel="preconnect" href="https://fonts.gstatic.com" />
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;800&family=Quicksand:wght@400;700&display=swap" rel="stylesheet" />
        <link href="/mq.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <div class="head-flex-container">
            <div class="left-flex-row">
                <h1>Mitarbeiterqualifikation</h1>
                <h1>Version 2.1 / 04.01.2021</h1>
            </div>
            <div class="right-flex-row">
                <div class="row-oriented-table rtable-2-cols">
                    <div class="rtable-cell no-border"><h1>Marina Inokuchi, Matr.-Nr. 1287686</h1></div>
                    <div class="rtable-cell no-border">
                        <img src="http://jigsaw.w3.org/css-validator/images/vcss-blue" alt="Valid CSS!" />
                    </div>
                </div>
            </div>
        </div>
        <div class="body-flex-container">
            <div class="sidebar-flex-container left-flex-row">
                <div class="menu-item menu-1">
                    <a href="/">Startseite</a>
                </div>
                <div class="menu-item menu-2">
                    <a href="/list_employees">Pflege Mitarbeiterdaten</a>
                    <a href="/list_trainings">Pflege Weiterbildungen</a>
                </div>
                <div class="menu-item menu-3">
                    <h2>Teilnahme</h2>
                    <ul>
                        <li><a href="/participation_employees">Sichtweise Mitarbeiter</a></li>
                        <li><a href="/participation_trainings">Sichtweise Weiterbildungen</a></li>
                    </ul>
                </div>
                <div class="menu-item menu-4">
                    <h2>Auswertungen</h2>
                    <ul>
                        <li><a href="/evaluation_employees">Mitarbeiter</a></li>
                        <li><a href="/evaluation_trainings">Weiterbildungen</a></li>
                        <li><a href="/evaluation_certificates">Zertifikate</a></li>
                    </ul>
                </div>
            </div>
            <div class="content-flex-container right-flex-row">
                <div class="content">
                    ${self.body()}
                </div>
            </div>
        </div>
        <script src="/mq.js"></script>
    </body>
</html>