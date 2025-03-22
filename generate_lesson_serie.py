from lib_templates import load_templates

templates = load_templates("templates")


def lesson_serie(id_link, lesson_title, lesson_count):
    lessons_html_string = ""
    for day in range(1, lesson_count + 1):
        lesson_id = id_link+'-'+str(day)
        lessons_html_string += templates["lesson"].substitute({'lesson_id': lesson_id, 'lesson_title': lesson_title+" "+str(day)})
    lesson_serie_html_string = templates["lesson_serie"].substitute({'lesson_serie_detail': lessons_html_string})
    return lesson_serie_html_string


lesson_id = "expertise"
lesson_title = "Expertise learning story"
lesson_count = 8

html_string = lesson_serie(lesson_id, lesson_title, lesson_count)

with open(lesson_id+ ".html", mode='w', encoding="utf-8") as file_late_list:
    file_late_list.write(html_string)
