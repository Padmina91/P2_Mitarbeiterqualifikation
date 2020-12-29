<%inherit file="base.tpl"/>

<%block name="body">
    <form action="/save" method="POST">
        <div class="row-oriented-table rtable-2-cols">
            <div class="rtable-cell">Name</div>
            <input type="text"
                        class="rtable-cell"
                        value=""
                        id="name"
                        name="name" required />
            <div class="rtable-cell">Vorname</div>
            <input type="text"
                        class="rtable-cell"
                        value=""
                        id="vorname"
                        name="vorname" required />
            <div class="rtable-cell">Akademische Grade</div>
            <input type="text"
                        class="rtable-cell"
                        value=""
                        id="akadGrade"
                        name="akadGrade" required />
            <div class="rtable-cell">Tätigkeit</div>
            <input type="text"
                        class="rtable-cell"
                        value=""
                        id="taetigkeit"
                        name="taetigkeit" required />
        </div>
        <div class="row-oriented-table rtable-2-cols">
            <div class="rtable-cell">
                <input type="submit" value="speichern" class="pseudo-button"/>
            </div>
            <div class="rtable-cell">
                <a class="pseudo-button" href="/list_employees">abbrechen</a>
            </div>
        </div>
    </form>
</%block>