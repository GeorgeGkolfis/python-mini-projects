from teachers import Teachers
from pupils import Pupils


class Lesson:
    def __init__(self, lesson_name="", lesson_id=-1):
        self.lesson_name = lesson_name
        self.lesson_id = lesson_id
        self.teacher_ids = []
        self.pupil_ids = []

    def from_dict(self, lesson_dict):
        self.lesson_name = lesson_dict["lesson_name"]
        self.lesson_id = lesson_dict["lesson_id"]
        self.teacher_ids = lesson_dict["teacher_ids"]
        self.pupil_ids = lesson_dict["pupil_ids"]

    def to_dict(self):
        lesson_dict = {"lesson_name": self.lesson_name,
                       "lesson_id": self.lesson_id,
                       "teacher_ids": self.teacher_ids,
                       "pupil_ids": self.pupil_ids,
                       }

        return lesson_dict

    def print_lesson_details(self, teachers, pupils):
        print(f"LESSON: {self.lesson_name}")
        print("=" * 8)
        print("TEACHERS: ")
        for teacher_id in self.teacher_ids:
            teacher = teachers.read_teacher_by_id(teacher_id)
            print(f"{teacher.first_name} {teacher.surname}")
        print("PUPILS: ")
        for pupil_id in self.pupil_ids:
            pupil = pupils.read_pupil_by_id(pupil_id)
            print(f"{pupil.first_name} {pupil.surname}")




