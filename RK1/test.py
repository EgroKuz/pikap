import unittest
from main import *


class Rk2_test(unittest.TestCase):
    languages = [
    ProgrammingLanguage(1, 'C++', 3, 2.8),
    ProgrammingLanguage(2, 'Python', 2, 13.4),
    ProgrammingLanguage(3, 'Java', 1, 14),
    ProgrammingLanguage(4, 'C', 4, 0.7),
    ProgrammingLanguage(5, 'Go', 4, 1.9),
    ProgrammingLanguage(6, 'PHP', 5, 7.1),
    ProgrammingLanguage(7, 'JavaScript', 4, 19.1)
    ]
    development_tools = [
        DevelopmentTool(1, 'IntelliJ IDEA'),
        DevelopmentTool(2, 'PyCharm'),
        DevelopmentTool(3, 'CLion'),
        DevelopmentTool(4, 'VSCode'),
        DevelopmentTool(5, 'PhP_sreda')
    ]
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
    def test_1(self):
        one_to_many = [(l.name, l.popularity, i.name)
                       for l in self.languages
                       for i in self.development_tools
                       if l.instr_id == i.id]
        res_11 = []
        for i in one_to_many:
            if i[0][0] == 'P':
                res_11.append(i)
        self.assertEqual(res_11, [('Java', 14, 'IntelliJ')])

    def test_2(self):
        one_to_many = [(l.name, l.popularity, i.name)
                       for l in self.languages
                       for i in self.development_tools
                       if l.instr_id == i.id]
        res_12_unsorted = []
        for instr in development_tools:
            devel_langs = list(filter(lambda i: i[2] == instr.name, one_to_many))
            if len(devel_langs) > 0:
                popularities = [popularity for _, popularity, _ in devel_langs]
            avg_popularity = sum(popularities) / len(popularities)
            res_12_unsorted.append((instr.name, avg_popularity))
        res_12 = sorted(res_12_unsorted, key=itemgetter(1))
        self.assertEqual(res_12, 'Среда разработки: CLion, Средняя популярность поддерживаемых языков: 2.80%Среда разработки: PhP_sreda, Средняя популярность поддерживаемых языков: 7.10%Среда разработки: VSCode, Средняя популярность поддерживаемых языков: 7.23%Среда разработки: PyCharm, Средняя популярность поддерживаемых языков: 13.40%Среда разработки: IntelliJ IDEA, Средняя популярность поддерживаемых языков: 14.00%')

    def test_3(self):
        many_to_many_temp = [(i.name, li.instr_id,  li.lang_id)
                             for i in self.development_tools
                             for li in self.language_tools
                             if i.id == li.instr_id
                             ]
        many_to_many = [(l.name, l.popularity, instr_name)
                        for instr_name, instr_id, lang_id in many_to_many_temp
                        for l in languages if l.id == lang_id
                        ]
        res = sorted(many_to_many, key=lambda item: (item[0], item[1]))
        self.assertEqual(res, [('C', 0.7, 'VSCode'), ('C++', 2.8, 'CLion'), ('Go', 1.9, 'VSCode'), ('Java', 14, 'IntelliJ IDEA'), ('Java', 14,
'VSCode'), ('JavaScript', 19.1, 'VSCode'), ('PHP', 7.1, 'PhP_sreda'), ('Python', 13.4, 'PyCharm')])

if __name__ == '__main__':
    unittest.main()
