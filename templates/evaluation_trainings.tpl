<%inherit file="base.tpl"/>
<%block name="body">
    % for training in data:
        <ul>
            <li>
                <h2>Erfolgreiche Teilnehmer an "${training[1]}", vom ${training[2]} bis ${training[3]}:</h2>
            </li>
        </ul>
        % if len(training[7]) > 0:
            <div class="row-oriented-table rtable-4-cols">
                <!-- Table Head -->
                <div class="rtable-head">Name</div>
                <div class="rtable-head">Vorname</div>
                <div class="rtable-head">akademische Grade</div>
                <div class="rtable-head">Tätigkeit</div>
                <!-- Table Content -->
                % for employee in training[7]:
                    <div class="rtable-cell">${employee[0]}</div>
                    <div class="rtable-cell">${employee[1]}</div>
                    <div class="rtable-cell">${employee[2]}</div>
                    <div class="rtable-cell">${employee[3]}</div>
                % endfor
            </div>
        % else:
            <h3>
                keine
            </h3>
        % endif
    % endfor
</%block>