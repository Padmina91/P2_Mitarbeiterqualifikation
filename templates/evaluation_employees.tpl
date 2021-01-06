<%inherit file="base.tpl"/>
<%block name="body">
    % for employee in data:
        <ul>
            <li>
                <h2>${employee[0]}, ${employee[1]}, ${employee[2]}, ${employee[3]}</h2>
            </li>
        </ul>
        <div class="row-oriented-table rtable-4-cols">
            <!-- Table Head -->
            <div class="rtable-head">Bezeichnung</div>
            <div class="rtable-head">Von</div>
            <div class="rtable-head">Bis</div>
            <div class="rtable-head">Teilnahmestatus</div>
            <!-- Table Content -->
            % for training in employee[4]:
                <div class="rtable-cell">${training[0]}</div>
                <div class="rtable-cell">${training[1]}</div>
                <div class="rtable-cell">${training[2]}</div>
                <div class="rtable-cell">${training[3]}</div>
            % endfor
        </div>
    % endfor
</%block>