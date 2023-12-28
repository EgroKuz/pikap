from operator import itemgetter

class ProgrammingLanguage:
    def __init__(self, id, name, instr_id, popularity):
        self.id = id
        self.name = name
        self.instr_id = instr_id
        self.popularity = popularity

class DevelopmentTool:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Language_Tool:
    def __init__(self, instr_id, lang_id):
        self.instr_id = instr_id
        self.lang_id = lang_id

# Данные о языках программирования
languages = [
    ProgrammingLanguage(1, 'C++', 3, 2.8),
    ProgrammingLanguage(2, 'Python', 2, 13.4),
    ProgrammingLanguage(3, 'Java', 1, 14),
    ProgrammingLanguage(4, 'C', 4, 0.7),
    ProgrammingLanguage(5, 'Go', 4, 1.9),
    ProgrammingLanguage(6, 'PHP', 5, 7.1),
    ProgrammingLanguage(7, 'JavaScript', 4, 19.1)
]

# Данные о средствах разработки
development_tools = [
    DevelopmentTool(1, 'IntelliJ IDEA'),
    DevelopmentTool(2, 'PyCharm'),
    DevelopmentTool(3, 'CLion' ),
    DevelopmentTool(4, 'VSCode'),
    DevelopmentTool(5, 'PhP_sreda')
]

# Связи между языками и средствами разработки
language_tools = [
    Language_Tool(1, 3),
    Language_Tool(2, 2),
    Language_Tool(3, 1),
    Language_Tool(4, 3),
    Language_Tool(4, 4),
    Language_Tool(4, 5),
    Language_Tool(5, 6),
    Language_Tool(4, 7)
]

def main():
    one_to_many = [(l.name, l.popularity, i.name)
                   for l in languages
                   for i in development_tools
                   if l.instr_id == i.id]
    many_to_many_temp = [(i.name, li.instr_id, li.lang_id)
                         for i in development_tools
                         for li in language_tools
                         if i.id == li.instr_id
                         ]
    many_to_many = [(l.name, l.popularity, instr_name)
                    for instr_name, instr_id, lang_id in many_to_many_temp
                    for l in languages if l.id == lang_id]
    print('Task 1')
    res_1 = []
    for i in one_to_many:
        if i[0][0] == 'P':
            res_1.append(i)
    print(res_1)

    print('Task 2')
    res_12_unsorted = []
    for instr in development_tools:
        devel_langs = list(filter(lambda i: i[2] == instr.name, one_to_many))
        if len(devel_langs) > 0:
            popularities = [popularity for _, popularity, _ in devel_langs]
        avg_popularity = sum(popularities) / len(popularities)
        res_12_unsorted.append((instr.name, avg_popularity))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1))
    for tool, avg_popularity in res_12:
        print(f"Среда разработки: {tool}, Средняя популярность поддерживаемых языков: {avg_popularity:.2f}%")

    print('Task 3')
    print(sorted(many_to_many, key=lambda item: (item[0], item[1])))


if __name__ == '__main__':
    main()