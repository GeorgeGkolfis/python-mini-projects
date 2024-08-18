from pupils import Pupils
from teachers import Teachers
from lessons import Lessons


def main():
    pupils = Pupils()
    teachers = Teachers()
    lessons = Lessons()

    while True:
        print("\n==============")
        print("     MENU      ")
        print("1. Manage Pupils")
        print("2. Manage Teachers")
        print("3. Manage Lessons")
        print("4. Exit")
        choice = int(input("Pick one: "))

        if choice == 1:
            print("\n==============")
            print("  PUPILS MENU   ")

            print("1. Create Pupil")
            print("2. Read Pupil")
            print("3. Update Pupil")
            print("4. Delete Pupil")
            pupils_choice = int(input("Pick one: "))

            if pupils_choice == 1:
                print("NEW PUPIL")
                print("=========")
                pupil = pupils.create_pupil()
                if pupil is None:
                    continue
                else:
                    print("\nNEW PUPIL")
                    print(pupil)

            elif pupils_choice == 2:
                print("\n==============")
                print(" SUBMENU (Read Pupil) ")
                print("1. Print pupil")
                print("2. Print all pupils (details)")
                print("3. Print all pupils (just the names)")
                print_choice = input("Give your choice: ")

                if print_choice.strip().isdigit():
                    print_choice = int(print_choice)
                else:
                    print("Wrong input!")
                    continue

                if print_choice == 1:
                    pupil_id = int(input("Give your id: "))
                    pupil = pupils.read_pupil_by_id(pupil_id)
                    if pupil is None:
                        print("Pupil doesnt exist(with this id).")
                    else:
                        print("   PUPIL   ")
                        print(pupil)

                elif print_choice == 2:
                    print(pupils)

                elif print_choice == 3:
                    pupils.print_pupils_names()

                else:
                    print("Wrong input!")
                    continue

            elif pupils_choice == 3:
                print("\n==============")
                print(" SUB-MENU (Update) ")
                print("1. Update pupil (search by id)")
                print("2. Update pupil (search by surname)")
                update_choice = input("Give your choice: ")

                if update_choice.strip().isdigit():
                    update_choice = int(update_choice)
                else:
                    print("Wrong input!")
                    continue

                if update_choice == 1:
                    pupil_id = int(input("Give id: "))
                    pupil = pupils.read_pupil_by_id(pupil_id)
                    if pupil is None:
                        print("There is not pupil with this id!")
                        continue
                elif update_choice == 2:
                    surname = input("Give surname: ")
                    matching_pupils = pupils.search_pupil_by_surname(surname)
                    if matching_pupils == []:     # [] == False, matching_pupils != [] the same as matching_pupils:
                        print("No matching pupils with this surname!")
                        continue
                    elif len(matching_pupils) == 1:
                        pupil = matching_pupils[0]
                    else:
                        for p in matching_pupils:
                            print(p)
                            print(f"id =  {p['id']}")
                            print("-" * 15)
                        pupil_id = int(input("Give id: "))
                        pupil = pupils.read_pupil_by_id(pupil_id)

                # update pupil
                pupils.pupil_update(pupil)

            elif pupils_choice == 4:
                print("\n==============")
                print(" SUB-MENU (Delete) ")
                print("1. Delete pupil (search by id)")
                print("2. Delete pupil (search by surname)")
                delete_choice = input("Give your choice: ")

                if delete_choice.strip().isdigit():
                    delete_choice = int(delete_choice)
                else:
                    print("Wrong input!")
                    continue

                if delete_choice == 1:
                    pupil_id = int(input("Give id: "))
                    pupil = pupils.read_pupil_by_id(pupil_id)
                    if pupil is None:
                        print("There is not pupil with this id!")
                        continue
                elif delete_choice == 2:
                    surname = input("Give surname: ")
                    matching_pupils = pupils.search_pupil_by_surname(surname)
                    if matching_pupils == []:  # [] == False, matching_pupils != [] the same as matching_pupils:
                        print("No matching pupils with this surname!")
                        continue
                    elif len(matching_pupils) == 1:
                        pupil = matching_pupils[0]
                    else:
                        for p in matching_pupils:
                            print(p)
                            print(f"id =  {p['id']}")
                            print("-" * 15)
                        pupil_id = int(input("Give id: "))
                        pupil = pupils.read_pupil_by_id(pupil_id)

                # delete pupil
                pupils.delete_pupil_by_id(pupil_id, lessons)

        elif choice == 2:
            print("\n==============")
            print("  TEACHERS MENU  ")

            print("1. Create Teacher")
            print("2. Read Teacher")
            print("3. Update Teacher")
            print("4. Delete Teacher")
            teachers_choice = int(input("Pick one: "))

            if teachers_choice == 1:
                first_name = input("Give name: ")
                surname = input("Give surname: ")
                teachers.create_teacher(first_name, surname)

            elif teachers_choice == 2:
                teacher_id = int(input("Give id: "))
                teacher = teachers.read_teacher_by_id(teacher_id)
                if teacher is None:
                    print("No teacher with this id!!!")
                else:
                    print(teacher)

            elif teachers_choice == 3:
                teacher_id = int(input("Give id: "))
                teachers.update_teacher(teacher_id)

            elif teachers_choice == 4:
                teacher_id = int(input("Give id: "))
                teachers.delete_teacher(teacher_id, lessons)

        elif choice == 3:
            print("\n==============")
            print("  LESSONS MENU  ")

            print("1. Create Lesson")
            print("2. Read Lesson")
            print("3. Update Lesson")
            print("4. Delete Lesson")
            lessons_choice = int(input("Pick one: "))

            if lessons_choice == 1:
                lesson_name = input("Give new lesson name: ")
                lessons.create_lesson(lesson_name)

            if lessons_choice == 2:
                lesson_id = int(input("Give lesson id: "))
                lesson = lessons.read_lesson_by_id(lesson_id)
                if lesson is None:
                    print("No such lesson exists!")
                else:
                    lesson.print_lesson_details(teachers, pupils)

            if lessons_choice == 3:
                lesson_id = int(input("Give lesson id: "))
                lessons.update_lesson(lesson_id, teachers, pupils)

            if lessons_choice == 4:
                lesson_id = int(input("Give id: "))
                lessons.delete_lesson(lesson_id)

        elif choice == 4:
            print("Bye bye!!!")
            pupils.save_pupils_data()
            teachers.save_teachers_data()
            lessons.save_lessons_data()
            break


main()
