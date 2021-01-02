<%inherit file="base.tpl"/>

<%block name="body">
    <div class="row-oriented-table rtable-5-cols">
    
        <!-- Table Head -->
        <div class="rtable-head">Name</div>
        <div class="rtable-head">Vorname</div>
        <div class="rtable-head">Akademische Grade</div>
        <div class="rtable-head">Tätigkeit</div>
        <div class="rtable-head">Aktion</div>

        <!-- Table Content -->
        % for key in employee_data:
        <div class="rtable-cell">${employee_data[key][0]}</div>
        <div class="rtable-cell">${employee_data[key][1]}</div>
        <div class="rtable-cell">${employee_data[key][2]}</div>
        <div class="rtable-cell">${employee_data[key][3]}</div>
        <div class="rtable-cell nested-row-oriented-table">
            <a class="pseudo-button nested-cell" href="/participation_employee/${key}">auswählen</a>
        </div>
        % endfor
    </div>
</%block>