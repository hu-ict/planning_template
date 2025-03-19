# planning_template
# Inleiding
Dit script genereert op basis van een csv-template een html-planning volgens de nieuwste Canvas-template. Als voorbeeld gebruiken we Canvas cursus: 
```
https://canvas.hu.nl/courses/45668
```
Het voordeel van onderstaande methode is dat bij wijzigingen van sprints de template makkelijk is aan te passen.
# Werking
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
## stap 3 - uitvoeren script
- Geef de variabele `template_filename` de juiste waarde van het opgeslagen template-bestand.
- Run het script, de html-tabel wordt gegenereerd,
- De html wordt opgeslagen in het bestand `planning.html`
## stap 4 - Canvas importeren
- Open de Canvas pagina waar de planning moet komen
- Edit de pagina
- Wijzig in html-view, knopje "<>"
- Kopieer de html uit `planning.html` naar de geopende Canvas-pagina.
- Sla de wijzigingen op

