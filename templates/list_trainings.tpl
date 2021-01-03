<%inherit file="base.tpl"/>
<%block name="body">
    <div class="row-oriented-table rtable-7-cols">
        <!-- Table Head -->
        <div class="rtable-head">Bezeichnung</div>
        <div class="rtable-head">Von</div>
        <div class="rtable-head">Bis</div>
        <div class="rtable-head">Beschreibung</div>
        <div class="rtable-head">maximale Teilnehmeranzahl</div>
        <div class="rtable-head">minimale Teilnehmeranzahl</div>
        <div class="rtable-head">Aktionen</div>
        <!-- Table Content -->
        % for key in training_data:
            <div class="rtable-cell">${training_data[key][0]}</div>
            <div class="rtable-cell">${training_data[key][1]}</div>
            <div class="rtable-cell">${training_data[key][2]}</div>
            <div class="rtable-cell">${training_data[key][3]}</div>
            <div class="rtable-cell">${training_data[key][4]}</div>
            <div class="rtable-cell">${training_data[key][5]}</div>
            <div class="rtable-cell nested-row-oriented-table">
                <a class="pseudo-button nested-cell" href="/edit_training/${key}">ändern</a>
                <a class="pseudo-button nested-cell delete-button" href="/delete_training/${key}">löschen</a>
                <a class="pseudo-button nested-cell" href="/show_training/${key}">anzeigen</a>
            </div>
        % endfor
    </div>
    <!-- Table Foot -->
    <div class="row-oriented-table rtable-1-cols">
        <div class="rtable-cell">
            <a class="pseudo-button" href="/add_training">erfassen</a>
        </div>
    </div>
</%block>