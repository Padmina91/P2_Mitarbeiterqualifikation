<%inherit file="base.tpl"/>

<%block name="body">
    <form action="/save_training" method="POST">
    <input type="hidden" value="${key}" id="id_param" name="id_param" />
        <div class="row-oriented-table rtable-2-cols">
            <div class="rtable-cell">Bezeichnung</div>
            <input type="text"
                        class="rtable-cell"
                        value="${data[0]}"
                        id="bezeichnung"
                        name="bezeichnung" required />
            <div class="rtable-cell">Von</div>
            <input type="date"
                        class="rtable-cell"
                        value="${data[1]}"
                        id="von"
                        name="von" required />
            <div class="rtable-cell">Bis</div>
            <input type="date"
                        class="rtable-cell"
                        value="${data[2]}"
                        id="bis"
                        name="bis" required />
            <div class="rtable-cell">Beschreibung</div>
            <input type="text"
                        class="rtable-cell"
                        value="${data[3]}"
                        id="beschreibung"
                        name="beschreibung" required />
            <div class="rtable-cell">maximale Teilnehmeranzahl</div>
            <input type="number"
                        class="rtable-cell"
                        value="${data[4]}"
                        id="maxTeiln"
                        name="maxTeiln" required />
            <div class="rtable-cell">minimale Teilnehmeranzahl</div>
            <input type="number"
                        class="rtable-cell"
                        value="${data[5]}"
                        id="minTeiln"
                        name="minTeiln" required />
        </div>
        <div class="row-oriented-table rtable-2-cols">
            <div class="rtable-cell">
                <input type="submit" value="speichern" class="pseudo-button"/>
            </div>
            <div class="rtable-cell">
                <a class="pseudo-button" href="/list_trainings">abbrechen</a>
            </div>
        </div>
    </form>
</%block>