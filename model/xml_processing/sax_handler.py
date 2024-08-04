import xml.sax
from model.entity.student import Student
from exception.xml_exception import XmlException


class SaxHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.students = []
        self.first_name = ''
        self.second_name = ''
        self.third_name = ''
        self.course = 0
        self.group = ''
        self.tasks = 0
        self.completed_tasks = 0
        self.language = ''
        self.current_data = ''

    def startElement(self, tag, attributes):
        self.current_data = ""
        if tag == "student":
            self.first_name = attributes["first_name"]
            self.second_name = attributes["second_name"]
            self.third_name = attributes["third_name"]

    def endElement(self, tag):
        if tag == "student":
            try:
                if self.language not in ["cxx", "Python", "Java"]:
                    raise ValueError("Not correct language")
                self.students.append(Student(0, self.first_name, self.second_name, self.third_name, int(self.course),
                                             self.group, int(self.tasks), int(self.completed_tasks), self.language))
            except ValueError as e:
                raise XmlException("Not correct data in file", e)
        elif tag == "course":
            self.course = self.current_data
        elif tag == "group":
            self.group = self.current_data
        elif tag == "tasks":
            self.tasks = self.current_data
        elif tag == "completed_tasks":
            self.completed_tasks = self.current_data
        elif tag == "language":
            self.language = self.current_data

    def characters(self, content):
        self.current_data = content.strip()
