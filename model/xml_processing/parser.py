from model.xml_processing.sax_handler import SaxHandler
from model.entity.student import Student
import xml.sax
import xml.etree.ElementTree as ElementTree
import xml.dom.minidom


class Parser:
    def __init__(self):
        pass

    @staticmethod
    def parse(path) -> list[Student]:
        handler = SaxHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(path)
        return handler.students

    @staticmethod
    def create(students: list[Student], path) -> None:
        root = ElementTree.Element("students")

        for student in students:
            student_elem = ElementTree.SubElement(root, "student")
            student_elem.set("first_name", student.first_name)
            student_elem.set("second_name", student.second_name)
            student_elem.set("third_name", student.third_name)

            course_elem = ElementTree.SubElement(student_elem, "course")
            course_elem.text = str(student.course)

            group_elem = ElementTree.SubElement(student_elem, "group")
            group_elem.text = student.group

            tasks_elem = ElementTree.SubElement(student_elem, "tasks")
            tasks_elem.text = str(student.tasks)

            completed_tasks_elem = ElementTree.SubElement(student_elem, "completed_tasks")
            completed_tasks_elem.text = str(student.completed_tasks)

            language_elem = ElementTree.SubElement(student_elem, "language")
            language_elem.text = student.language

        tree = ElementTree.ElementTree(root)

        xml_string = ElementTree.tostring(root, encoding="utf-8")
        dom = xml.dom.minidom.parseString(xml_string)
        pretty_xml_string = dom.toprettyxml(indent="  ")

        with open(path, "w", encoding="utf-8") as f:
            f.write(pretty_xml_string)
