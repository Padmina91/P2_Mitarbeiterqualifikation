<%inherit file="base.tpl"/>
<%block name="body">
    % if len(data[0]) > 0:
        <h1>Laufende Weiterbildungen</h1>
        <div class="row-oriented-table rtable-7-cols">
            <!-- Table Head -->
            <div class="rtable-head">Bezeichnung</div>
            <div class="rtable-head">Von</div>
            <div class="rtable-head">Bis</div>
            <div class="rtable-head">Beschreibung</div>
            <div class="rtable-head">minimale Teilnehmeranzahl</div>
            <div class="rtable-head">maximale Teilnehmeranzahl</div>
            <div class="rtable-head">Aktion</div>
            <!-- Table Content -->
            % for training in data[0]:
                <div class="rtable-cell">${training[1]}</div>
                <div class="rtable-cell">${training[2]}</div>
                <div class="rtable-cell">${training[3]}</div>
                <div class="rtable-cell">${training[4]}</div>
                <div class="rtable-cell">${training[6]}</div>
                <div class="rtable-cell">${training[5]}</div>
                <div class="rtable-cell nested-row-oriented-table">
                    <a class="pseudo-button nested-cell" href="/participation_training/${training[0]}">auswählen</a>
                </div>
            % endfor
        </div>
    % endif
    % if len(data[1]) > 0:
        <h1>Abgeschlossene Weiterbildungen</h1>
        <div class="row-oriented-table rtable-7-cols">
            <!-- Table Head -->
            <div class="rtable-head">Bezeichnung</div>
            <div class="rtable-head">Von</div>
            <div class="rtable-head">Bis</div>
            <div class="rtable-head">Beschreibung</div>
            <div class="rtable-head">minimale Teilnehmeranzahl</div>
            <div class="rtable-head">maximale Teilnehmeranzahl</div>
            <div class="rtable-head">Aktion</div>
            <!-- Table Content -->
            % for training in data[1]:
                <div class="rtable-cell">${training[1]}</div>
                <div class="rtable-cell">${training[2]}</div>
                <div class="rtable-cell">${training[3]}</div>
                <div class="rtable-cell">${training[4]}</div>
                <div class="rtable-cell">${training[6]}</div>
                <div class="rtable-cell">${training[5]}</div>
                <div class="rtable-cell nested-row-oriented-table">
                    <a class="pseudo-button nested-cell" href="/participation_training/${training[0]}">auswählen</a>
                </div>
            % endfor
        </div>
    % endif
</%block>