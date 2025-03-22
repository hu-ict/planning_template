# Canvas templating
# Inleiding
Deze repo bevat twee Python script die html genereerd t.b.v. de HBO-ICT-2026 Canvas look-and-feel.
- Genereren van een planning voor de hoofdpagina
- Genereren van een lessenreeks als onderdeel van de student journey

Als voorbeeld gebruiken we Canvas cursus:
```
https://canvas.hu.nl/courses/45668
```
# Werking generate_planning.py
Dit script genereert op basis van een csv-template een html-planning volgens de nieuwste Canvas-template. Het voordeel van deze methode is dat bij wijzigingen van sprints de template makkelijk is aan te passen.
## stap 1 - course_id
- Vul boven in het script de juiste canvas cursus `canvas_id`
- De links in het html bestand verwijzen dan naar de goede cursus
## Stap 2 - template
- Open het template bestand, bijvoorbeeld: `planning_template_sep25.csv`
- Sla dit bestand op met een nieuwe naam, bijvoorbeeld: `planning_inno_sep25.csv`
- Benoem de sprintnummers, als een sprint over meerdere weken loopt krijgt elke week het sprintnummer,
- Vakantieweken krijgen geen sprintnummer
- De weeknummers en vakanties staan al goed
- Geef de dagen een goed label, dit zijn de kolommen "Ma" tm "Vr"
- Als er doorgeklikt moet worden, vul in de kolommen "L_Ma" tm "L_Vr" de juiste link-pagina in. De naam van de pagina is het deel in de url achter `\pages\`. Als je het veld leeg laat wordt er geen link opgenomen.
- De velden "D_Ma" tm "D_Vr" kunnen gebruikt worden om ook een datum in de planning op te nemen.
- Sla het bestand nu op
## Stap 3 - uitvoeren script
- Geef de variabele `template_filename` de juiste waarde van het opgeslagen template-bestand.
- Run het script `generate_planning.py`, de html-tabel wordt gegenereerd,
- De html wordt opgeslagen in het bestand `planning.html`
## Stap 4 - Canvas importeren
- Open de Canvas pagina waar de planning moet komen
- Edit de pagina
- Wijzig in html-view, knopje "<>"
- Kopieer de html uit `planning.html` naar de geopende Canvas-pagina.
- Sla de wijzigingen op

# Werking generate_lesson_serie
Dit script rendert een html pagina met een lessenreeks op basis van twee html-templates. De templates zijn aan te passen naar eigen wens. 
# stap 1 - Templates
- Ga naar de directory `templates` en open de template `template_lesson.html`,
- Pas deze template naar behoefte aan,
- Zorg dat de twee placeholders aanwezig blijven `$lesson_id` en `$lesson_title`,
- De kop en inleiding worden in een tweede html-template beschreven, open `template_lesson_serie.html`,
- Pas deze aan je behoeft aan,
- Zorg dat de placeholder `$lesson_serie_detail` aanwezig blijft,
# stap 2 - Script
- Open het script `generate_lesson_serie.py`
- Pas de variabelen aan voor eigen gebruik:
```lession_id = "expertise"
lesson_title = "Expertise learning story"
lesson_count = 8
```
- De `lesson_id` variabele kan je gebruiken als verwijzing (link) in de planningtabel, bijvoorbeeld: `expertise#expertise-1` in het csv-veld `L_Ma`,
- `lesson_title` wordt gebruikt om een lesdag van een titel te voorzien,
- `lesson_count` geeft aan hoeveel lesdagen gegenereerd moeten worden,
- Script is nu klaar om uitgevoerd te worden
- Resultaat komt in `[lesson_id].html`, in het voorbeeld: `expertise.html`

