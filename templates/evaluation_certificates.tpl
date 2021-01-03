<%inherit file="base.tpl"/>
<%block name="body">
    % for certificate in data:
        <h2><li>
            Mitarbeiter mit dem Zertifikat "${certificate[1]}":
        </h2></li>
        % if len(certificate[2]) > 0:
            <div class="row-oriented-table rtable-4-cols">
                <!-- Table Head -->
                <div class="rtable-head">Name</div>
                <div class="rtable-head">Vorname</div>
                <div class="rtable-head">akademische Grade</div>
                <div class="rtable-head">Tätigkeit</div>
                <!-- Table Content -->
                % for employee in certificate[2]:
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