<%inherit file="base.tpl"/>

<%block name="body">
    <div class="row-oriented-table rtable-5-cols">
        <div class="rtable-head">Name</div>
        <div class="rtable-head">Vorname</div>
        <div class="rtable-head">Akademische Grade</div>
        <div class="rtable-head">Tätigkeit</div>
        <div class="rtable-head">Aktionen</div>

        <div class="rtable-cell">Platzhalter1 Name</div>
        <div class="rtable-cell">Platzhalter1 Vorname</div>
        <div class="rtable-cell">Platzhalter1 Akademische Grade</div>
        <div class="rtable-cell">Platzhalter1 Tätigkeit</div>
        <div class="rtable-cell nested-row-oriented-table">
            <a class="pseudo-button nested-cell" href="">ändern</a>
            <a class="pseudo-button nested-cell" href="">löschen</a>
            <a class="pseudo-button nested-cell" href="">anzeigen</a>
        </div>

        <div class="rtable-cell">Platzhalter2 Name</div>
        <div class="rtable-cell">Platzhalter2 Vorname</div>
        <div class="rtable-cell">Platzhalter2 Akademische Grade</div>
        <div class="rtable-cell">Platzhalter2 Tätigkeit</div>
        <div class="rtable-cell nested-row-oriented-table">
            <a class="pseudo-button nested-cell" href="">ändern</a>
            <a class="pseudo-button nested-cell" href="">löschen</a>
            <a class="pseudo-button nested-cell" href="">anzeigen</a>
        </div>
    </div>

    <div class="row-oriented-table rtable-1-cols">
        <div class="rtable-cell">
            <a class="pseudo-button" href="/add_employee">erfassen</a>
        </div>
    </div>
</%block>