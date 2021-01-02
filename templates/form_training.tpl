<%inherit file="base.tpl"/>

<%block name="body">
    <form action="/save_training" id="training-form" name="training-form" class="training-form" method="POST">
        <input type="hidden" value="${key}" id="id_param" name="id_param" />
        <div class="row-oriented-table rtable-2-cols">
            <div class="rtable-cell">Bezeichnung</div>
            <input type="text"
                        class="rtable-cell"
                        value="${training_data[0]}"
                        id="bezeichnung"
                        name="bezeichnung" required />
            <div class="rtable-cell">Von</div>
            <input type="date"
                        class="rtable-cell"
                        value="${training_data[1]}"
                        id="von"
                        name="von" required />
            <div class="rtable-cell">Bis</div>
            <input type="date"
                        class="rtable-cell"
                        value="${training_data[2]}"
                        id="bis"
                        name="bis" required />
            <div class="rtable-cell">Beschreibung</div>
            <input type="text"
                        class="rtable-cell"
                        value="${training_data[3]}"
                        id="beschreibung"
                        name="beschreibung" required />
            <div class="rtable-cell">maximale Teilnehmeranzahl</div>
            <input type="number"
                        class="rtable-cell"
                        value="${training_data[4]}"
                        id="maxTeiln"
                        name="maxTeiln" required />
            <div class="rtable-cell">minimale Teilnehmeranzahl</div>
            <input type="number"
                        class="rtable-cell"
                        value="${training_data[5]}"
                        id="minTeiln"
                        name="minTeiln" required />
            <div class="rtable-cell">Haupt-Qualifikation</div>
            <% qualification_existing = len(training_data[6]) > 0 %>
            % if qualification_existing:
            <input type="text"
                        class="rtable-cell"
                        value="${training_data[6][0]}"
                        id="qualification0"
                        name="qualification0" required />
            % else:
            <input type="text"
                        class="rtable-cell"
                        value=""
                        id="qualification0"
                        name="qualification0" required />
            % endif
            <div class="rtable-cell">Zertifikat (optional)</div>
            <% certificate_existing = len(training_data[7]) > 0 %>
            % if certificate_existing:
            <input type="text"
                        class="rtable-cell"
                        value="${training_data[7][0]}"
                        id="zertifikat"
                        name="zertifikat" />
            % else:
            <input type="text"
                        class="rtable-cell"
                        value=""
                        id="zertifikat"
                        name="zertifikat" />
            % endif
        </div>

        <% training_already_saved = key != None %>
        % if training_already_saved:
        <div class="row-oriented-table rtable-2-cols">
            <!-- Table Head -->
            <div class="rtable-head">Weitere Qualifikationen</div>
            <div class="rtable-head">Aktionen</div>

            <!-- Table Content -->
            <% i = 0 %>
            % for qual in training_data[6]:
                % if i != 0:
                    <div class="rtable-cell">${qual}</div>
                    <div class="rtable-cell nested-row-oriented-table">
                        <a class="pseudo-button nested-cell" href="/edit_qualification/${key}/${i}">ändern</a> <!-- TODO: Ändern-Formular implementieren -->
                        <a class="pseudo-button nested-cell delete-button" href="/delete_qualification/${key}/${i}">löschen</a> <!-- TODO: löschen implementieren -->
                    </div>
                % endif
                <% i += 1 %>
            % endfor
        </div>

        <div class="row-oriented-table rtable-1-cols">
            <div class="rtable-cell">
                <a href="/add_qualification/${key}" class="pseudo-button">weitere Qualifikation erfassen</a>
            </div>
        </div>
        % endif

        <div class="row-oriented-table rtable-2-cols">
            <div class="rtable-cell">
                <a href="/list_trainings" class="pseudo-button submit-button">speichern</a>
            </div>
            <div class="rtable-cell">
                <a class="pseudo-button" href="/list_trainings">abbrechen</a>
            </div>
        </div>
    </form>
</%block>