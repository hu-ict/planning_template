from string import Template


def load_templates(template_path):
    templates = {}
    with open(template_path + '//template_lesson.html', mode='r', encoding="utf-8") as file_template:
        string_html = file_template.read()
        templates["lesson"] = Template(string_html)

    with open(template_path + '//template_lesson_serie.html', mode='r', encoding="utf-8") as file_template:
        string_html = file_template.read()
        templates["lesson_serie"] = Template(string_html)

    with open(template_path + '//template_planning.html', mode='r', encoding="utf-8") as file_template:
        string_html = file_template.read()
        templates["planning"] = Template(string_html)

    return templates