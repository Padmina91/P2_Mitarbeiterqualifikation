<%inherit file="base.tpl"/>

<%block name="body">
    <h1>${training_data[0]}, von ${training_data[1]} bis ${training_data[2]}</h1>
    <h2>weitere Qualifikation Nummer ${int(index)}:</h2>
    <form action="/save_qualification" method="POST">
        <input type="hidden" value="${key}" id="id_param" name="id_param" />
        <input type="hidden" value="${index}" id="index" name="index" />
        <div class="row-oriented-table rtable-2-cols">
            <div class="rtable-cell">Bezeichnung</div>
            <% qualification_existing = len(training_data[6]) > int(index) %>
            % if qualification_existing:
            <input type="text"
                        class="rtable-cell"
                        value="${training_data[6][int(index)]}"
                        id="bezeichnung"
                        name="bezeichnung" required />
            % else:
            <input type="text"
                        class="rtable-cell"
                        value=""
                        id="bezeichnung"
                        name="bezeichnung" required />
            % endif
        </div>
        <div class="row-oriented-table rtable-2-cols">
            <div class="rtable-cell">
                <input type="submit" value="speichern" class="pseudo-button"/>
            </div>
            <div class="rtable-cell">
                <a class="pseudo-button" href="/edit_training/${key}">abbrechen</a>
            </div>
        </div>
</%block>