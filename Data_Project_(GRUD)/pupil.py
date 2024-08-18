class Pupil:
    def __init__(self, pupil_id="", first_name="", surname="",
                 fathers_name="", age=-1, class_name="", id_number=None,):
        self.pupil_id = pupil_id
        self.first_name = first_name
        self.surname = surname
        self.fathers_name = fathers_name
        self.age = age
        self.class_name = class_name
        self.id_number = id_number

    def from_dict(self, pupil_dict):
        self.pupil_id = pupil_dict["pupil_id"]
        self.first_name = pupil_dict["first_name"]
        self.surname = pupil_dict["surname"]
        self.fathers_name = pupil_dict["fathers_name"]
        self.age = pupil_dict["age"]
        self.class_name = pupil_dict["class_name"]
        if "id_number" in pupil_dict:
            self.id_number = pupil_dict["id_number"]

    def to_dict(self):
        pupil_dict = {"pupil_id": self.pupil_id,
                      "first_name": self.first_name,
                      "surname": self.surname,
                      "fathers_name": self.fathers_name,
                      "age": self.age,
                      "class_name": self.class_name}
        if self.id_number is not None:
            pupil_dict["id_number"] = self.id_number
        return pupil_dict

    def __str__(self):
        st = f"\nName           : {self.first_name}"
        st += f"\nSurname        : {self.surname}"
        st += f"\nFathers name   : {self.fathers_name}"
        st += f"\nAge            : {self.age}"
        st += f"\nClass          : {self.class_name}"
        if self.id_number is not None:
            st += f"\nId card number : {self.id_number}"
        return st
