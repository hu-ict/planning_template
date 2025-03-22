import csv

from lib_templates import load_templates

week_row_colors = ["#ffffff", "#f0f0f0"]
sprint_colors = ["#e6302b", "#00a1e1"]
week_days = ["ma", "di", "wo", "do", "vr"]
course_id = "44850"
template_filename = "planning_inno_sep25.csv"
planning_filename = "planning.html"
html_templates = load_templates("templates")


def get_row_color(index):
    return week_row_colors[index % 2]


def get_sprint_color(sprint):
    return sprint_colors[sprint % 2 ]


def determine_sprints(weeks):
    sprints = {}
    for week in weeks:
        if week["sprint"] != "":
            if week["sprint"] in sprints:
                sprints[week["sprint"]] += 1
            else:
                sprints[week["sprint"]] = 1
    return sprints


def get_sprint_rowspan(sprints, last_sprint, sprint, sprint_color):
    if sprint == "":
        return '<td></td>'
    elif last_sprint != sprint:
        return '<td style="text-align: center; border-top: '+sprint_color+' 3px solid; color: white; background-color: '+sprint_color+';" rowspan='+str(sprints[str(sprint)])+'><strong>'+str(sprint)+'</strong></td>'
    else:
        return ""


def read_weeks(a_filename):
    print('READ WEEKS:', a_filename)
    weeks = []
    with open(a_filename, 'r', encoding="utf-8") as csvfile:
        for line in csv.DictReader(csvfile, delimiter=";"):
            # print(line)
            week = {'sprint': line['Sprint'], 'week': line['Week'], 'ma': line['Ma'], 'di': line['Di'], 'wo': line['Wo'], 'do': line['Do'], 'vr': line['Vr'],
                    'l_ma': line['L_Ma'], 'l_di': line['L_Di'], 'l_wo': line['L_Wo'], 'l_do': line['L_Do'], 'l_vr': line['L_Vr'],
                    'd_ma': line['D_Ma'], 'd_di': line['D_Di'], 'd_wo': line['D_Wo'], 'd_do': line['D_Do'], 'd_vr': line['D_Vr']}
            weeks.append(week)
    return weeks


def render_planning(weeks):
    planning_html_string = ""
    index = 0
    last_sprint = '-1'
    for week in weeks:
        print(week)
        sprint = week["sprint"]

        if week["sprint"] == "":
            row_color = "#d0d0d0"
            sprint_color = row_color
        else:
            row_color = get_row_color(index)
            sprint_color = get_sprint_color(int(sprint))

        planning_html_string +='\n<tr style="background-color: ' + row_color + ';">'
        sprint_html = get_sprint_rowspan(sprints, last_sprint, sprint, sprint_color)
        if len(sprint_html) > 10:
            sprint_border = "border-top: 3px solid " + sprint_color + ";"
        else:
            sprint_border = ""
        planning_html_string += '\n' + sprint_html
        planning_html_string += '\n<td style="text-align: center; ' + sprint_border + '">' + week['week'] + '</td>'
        if sprint == "":
            planning_html_string += '\n<td style="text-align: center;" colspan="5">' + week["ma"] + '</td>'
        else:
            for day in week_days:
                if "d_" + day in week and week["d_" + day] != "":
                    datum_label = '<span style="font-size: 0.8em;">' + week["d_" + day] + '</span><br>'
                else:
                    datum_label = ""
                if week_days[-1] == day:
                    # laatste dag is de rechter cell in de tabel en dus ook de rechterrand van de tabel
                    border_right = "border-right: 3px solid" + sprint_color + ";"
                else:
                    border_right = ""
                if "@" in week[day]:
                    # vakantiedag, geen link en donkergrijs
                    planning_html_string += '\n<td style="background-color: #d0d0d0; ' + sprint_border + ' ' + border_right + '">' + week[day].replace("@", "") + '</td>'
                else:
                    if week["l_" + day] != "":
                        # link opnemen bij het onderwerp van de dag
                        anchor = '<a title="' + week[
                            "l_" + day] + '" href="https://canvas.hu.nl/courses/' + course_id + '/pages/' + week[
                                     "l_" + day] + '" data-course-type="wikiPages" data-published="true" data-api-endpoint="https://canvas.hu.nl/api/v1/courses/' + course_id + '/pages/' + \
                                 week["l_" + day] + '" data-api-returntype="Page">' + week[day] + '</a>'
                        planning_html_string += '\n<td style="' + sprint_border + ' ' + border_right + '">' + datum_label + anchor + '</td>'
                    else:
                        planning_html_string += '\n<td style="' + sprint_border + ' ' + border_right + '">' + datum_label + week[day] + '</td>'

        planning_html_string += '\n</tr>'
        if week["sprint"] != "":
            index += 1
        last_sprint = sprint
    planning_table_html_string = html_templates["planning"].substitute({'planning': planning_html_string})
    return planning_table_html_string



weeks = read_weeks(template_filename)
sprints = determine_sprints(weeks)
planning_html = render_planning(weeks)
with open(planning_filename, mode='w', encoding="utf-8") as outfile:
    outfile.write(planning_html)
