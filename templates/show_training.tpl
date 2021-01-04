<%inherit file="base.tpl"/>
<%block name="body">
    <h2>Weiterbildung "${data[0]}", vom ${data[1]} bis ${data[2]}</h2>
    % if len(data[3]) > 0:
        <h3>Zertifikat: ${data[3][0]}</h3>
    % else:
        <h3>Zertifikat: -</h3>
    % endif
    % if len(data[4]) == 1:
        <h3>Qualifikation:</h3>
    % else:
        <h3>Qualifikationen:</h3>
    % endif
    <ul>
        % for qualification in data[4]:
            <li>${qualification}</li>
        % endfor
    </ul>
    <h2>Teilnahmen:</h2>
    <div class="row-oriented-table rtable-5-cols">
        <!-- Table Head -->
        <div class="rtable-head">Name</div>
        <div class="rtable-head">Vorname</div>
        <div class="rtable-head">Akademische Grade</div>
        <div class="rtable-head">Tätigkeit</div>
        <div class="rtable-head">Teilnahmestatus</div>
        <!-- Table Content -->
        % if len(data[5]) > 0:
            % for employee in data[5]:
                <div class="rtable-cell">${employee[0]}</div>
                <div class="rtable-cell">${employee[1]}</div>
                <div class="rtable-cell">${employee[2]}</div>
                <div class="rtable-cell">${employee[3]}</div>
                <div class="rtable-cell">${employee[4]}</div>
            % endfor
        % else:
            <h3>keine</h3>
        % endif
    </div>
    <!-- Table Foot -->
    <div class="row-oriented-table rtable-1-cols">
        <div class="rtable-cell no-border">
            <a class="pseudo-button" href="/list_trainings">zurück</a>
        </div>
    </div>
</%block>