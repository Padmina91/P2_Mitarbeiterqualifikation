<%inherit file="base.tpl"/>

<%block name="body">
    <div class="row-oriented-table rtable-7-cols">
        <div class="rtable-head">Bezeichnung</div>
        <div class="rtable-head">Von</div>
        <div class="rtable-head">Bis</div>
        <div class="rtable-head">Beschreibung</div>
        <div class="rtable-head">maximale Teilnehmeranzahl</div>
        <div class="rtable-head">minimale Teilnehmeranzahl</div>
        <div class="rtable-head">Aktionen</div>

        <div class="rtable-cell">Platzhalter1 Bezeichnung</div>
        <div class="rtable-cell">Platzhalter1 Von</div>
        <div class="rtable-cell">Platzhalter1 Bis</div>
        <div class="rtable-cell">Platzhalter1 Beschreibung</div>
        <div class="rtable-cell">Platzhalter1 maximale Teilnehmeranzahl</div>
        <div class="rtable-cell">Platzhalter1 minimale Teilnehmeranzahl</div>
        <div class="rtable-cell nested-row-oriented-table">
            <a class="pseudo-button nested-cell" href="">ändern</a>
            <a class="pseudo-button nested-cell" href="">löschen</a>
            <a class="pseudo-button nested-cell" href="">anzeigen</a>
        </div>

        <div class="rtable-cell">Platzhalter2 Bezeichnung</div>
        <div class="rtable-cell">Platzhalter2 Von</div>
        <div class="rtable-cell">Platzhalter2 Bis</div>
        <div class="rtable-cell">Platzhalter2 Beschreibung</div>
        <div class="rtable-cell">Platzhalter2 maximale Teilnehmeranzahl</div>
        <div class="rtable-cell">Platzhalter2 minimale Teilnehmeranzahl</div>
        <div class="rtable-cell nested-row-oriented-table">
            <a class="pseudo-button nested-cell" href="">ändern</a>
            <a class="pseudo-button nested-cell" href="">löschen</a>
            <a class="pseudo-button nested-cell" href="">anzeigen</a>
        </div>
    </div>

    <div class="row-oriented-table rtable-1-cols">
        <div class="rtable-cell">
            <a class="pseudo-button" href="/add_training">erfassen</a>
        </div>
    </div>
</%block>