# planning_template
# Inleiding
Dit script genereert op basis van een csv-template een html-planning volgens de nieuwste Canvas-template. Als voorbeeld gebruiken we Canvas cursus: 
```
https://canvas.hu.nl/courses/45668
```
# Werking
## stap 1 course_id
- Vul boven in het script de juiste canvas cursus `canvas_id`
- De links in het html bestand verwijzen dan naar de goede cursus

## Stap 2 - template
- Open het template bestand, bijvoorbeeld: `planning_template_sep25.csv`
- Sla dit bestand op met een nieuwe naam, bijvoorbeeld: `planning_inno_sep25.csv`
- Benoem de sprintnummers, als een sprint over meerdere weken loopt krijgt elke week het sprintnummer,
- Vakantieweken krijgen geen sprintnummer
- De weeknummers en vakanties staan al goed
- Geef de dagen een goed label, dit zijn de kolommen "Ma" tm "Vr"
- Als er doorgeklikt moet worden, vul in de kolommen "L_Ma" tm "L_Vr" de juiste link-pagina in.
-- De naam van de pagina is het deel in de url achter `\pages\`.
-- Als je het veld leeg laat wordt er geen link opgenomen
