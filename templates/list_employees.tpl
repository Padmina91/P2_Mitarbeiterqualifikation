<%inherit file="base.tpl"/>

<%block name="body">
    <div class="row-oriented-table rtable-5-cols">
        <!-- Table Head -->
        <div class="rtable-head">Name</div>
        <div class="rtable-head">Vorname</div>
        <div class="rtable-head">Akademische Grade</div>
        <div class="rtable-head">Tätigkeit</div>
        <div class="rtable-head">Aktionen</div>

        <!-- Table Content -->
        % for key in data:
        <div class="rtable-cell">${data[key][0]}</div>
        <div class="rtable-cell">${data[key][1]}</div>
        <div class="rtable-cell">${data[key][2]}</div>
        <div class="rtable-cell">${data[key][3]}</div>
        <div class="rtable-cell nested-row-oriented-table">
            <a class="pseudo-button nested-cell" href="/edit_employee/${key}">ändern</a>
            <a class="pseudo-button nested-cell delete-button" href="/delete_employee//${key}">löschen</a>
            <a class="pseudo-button nested-cell" href="show_employee/${key}">anzeigen</a>
        </div>
        % endfor
    </div>

    <!-- Table Foot -->
    <div class="row-oriented-table rtable-1-cols">
        <div class="rtable-cell">
            <a class="pseudo-button" href="/add_employee">erfassen</a>
        </div>
    </div>
</%block>