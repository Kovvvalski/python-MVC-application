from controller.controller import StudentsController
from view.students_view import StudentsView
from model.repository.student_db_repository import StudentDbRepository
from dbconnection.connection_pool import connection
from model.service.student_service import StudentService

if __name__ == '__main__':
    view = StudentsView()
    rep = StudentDbRepository(connection)
    service = StudentService(rep)
    ctrl = StudentsController(service, view)
    ctrl.start()
