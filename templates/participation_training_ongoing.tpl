<%inherit file="base.tpl"/>

<%block name="body">

    <h1>
        Laufende Weiterbildungen
    </h1>

    <div class="row-oriented-table rtable-6-cols">
        <!-- Table Head -->
        <div class="rtable-head">Name</div>
        <div class="rtable-head">Vorname</div>
        <div class="rtable-head">Akademische Grade</div>
        <div class="rtable-head">Tätigkeit</div>
        <div class="rtable-head">Teilnahmestatus</div>
        <div class="rtable-head">Aktionen</div>

        <!-- Table Content -->
        % for employee in data:
        <div class="rtable-cell">${employee[1]}</div>
        <div class="rtable-cell">${employee[2]}</div>
        <div class="rtable-cell">${employee[3]}</div>
        <div class="rtable-cell">${employee[4]}</div>
        <div class="rtable-cell">${employee[5]}</div>
        <div class="rtable-cell nested-row-oriented-table">
            <a class="pseudo-button nested-cell cancel-participation" href="/cancel_participation/${key}/${employee[0]}">Teilnahme abbrechen</a>
        </div>
        % endfor
    </div>

    <!-- Table Foot -->
    <div class="row-oriented-table rtable-1-cols">
        <div class="rtable-cell">
            <a class="pseudo-button" href="/participation_trainings">zurück</a>
        </div>
    </div>

</%block>