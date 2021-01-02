<%inherit file="base.tpl"/>

<%block name="body">
    <h1>
        ${employee_data[0]}, ${employee_data[1]}, akademische Grade: ${employee_data[2]}, Tätigkeit: ${employee_data[3]}
    </h1>

    % if len(data[0]) > 0:
    <h2>
        Weiterbildung, zu denen eine Anmeldung möglich ist
    </h2>
    <div class="row-oriented-table rtable-5-cols">

         <!-- Table Head -->
        <div class="rtable-head">Bezeichnung</div>
        <div class="rtable-head">Von</div>
        <div class="rtable-head">Bis</div>
        <div class="rtable-head">Beschreibung</div>
        <div class="rtable-head">Aktion</div>

        <!-- Table Content -->
        % for future_training in data[0]:
        <div class="rtable-cell">${future_training[1]}</div>
        <div class="rtable-cell">${future_training[2]}</div>
        <div class="rtable-cell">${future_training[3]}</div>
        <div class="rtable-cell">${future_training[4]}</div>
        <div class="rtable-cell nested-row-oriented-table">
            <a class="pseudo-button nested-cell register-training" href="/register_for_training/${key}/${future_training[0]}">zu Weiterbildung anmelden</a>
        </div>
        % endfor
    </div>
    % endif

    % if len(data[1]) > 0:
    <h2>
        Angemeldete Weiterbildungen
    </h2>

    <div class="row-oriented-table rtable-5-cols">

        <!-- Table Head -->
        <div class="rtable-head">Bezeichnung</div>
        <div class="rtable-head">Von</div>
        <div class="rtable-head">Bis</div>
        <div class="rtable-head">Beschreibung</div>
        <div class="rtable-head">Aktion</div>

        <!-- Table Content -->
        % for registered_training in data[1]:
        <div class="rtable-cell">${registered_training[1]}</div>
        <div class="rtable-cell">${registered_training[2]}</div>
        <div class="rtable-cell">${registered_training[3]}</div>
        <div class="rtable-cell">${registered_training[4]}</div>
        <div class="rtable-cell nested-row-oriented-table">
            <a class="pseudo-button nested-cell cancel-training" href="/cancel_registration/${key}/${registered_training[0]}">Anmeldung stornieren</a>
        </div>
        % endfor
    </div>
    % endif

    <!-- Table Foot -->
    <div class="row-oriented-table rtable-1-cols">
        <div class="rtable-cell">
            <a class="pseudo-button" href="/participation_employees">zurück</a>
        </div>
    </div>
</%block>