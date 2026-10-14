from abc import ABC, abstractmethod
import os
import pandas as pd

class Person(ABC):
    def __init__(self, name: str):
        self._name = name

    def display_details(self):
        pass

class Student(Person):
    def __init__(self, student_id: str, name: str, marks: list):
        super().__init__(name)
        self.__student_id = str(student_id)  
        self.__marks = marks                 

    def get_student_id(self) -> str:
        return self.__student_id

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        if name.strip():
            self._name = name

    def get_marks(self) -> list:
        return self.__marks

    def set_marks(self, marks: list):
        if all(0 <= m <= 100 for m in marks):
            self.__marks = marks

    def calculate_average(self) -> float:
        if not self.__marks:
            return 0.0
        return sum(self.__marks) / len(self.__marks)

    def display_details(self):
        avg = self.calculate_average()
        marks_str = ", ".join(f"{m:.1f}" for m in self.__marks)
        print(f"ID: {self.__student_id} | Name: {self._name} | Marks: [{marks_str}] | Average: {avg:.2f}")


class StudentManager:
    def __init__(self, filename="student_records_100.csv"):
        self.filename = filename
        self.students = {}
        self.load_from_csv()

    def load_from_csv(self):
        if not os.path.exists(self.filename):
            print(f"Warning: {self.filename} not found. Starting with an empty record list.")
            return
        try:
            df = pd.read_csv(self.filename)
            for _, row in df.iterrows():
                s_id = str(row['Student_ID'])
                name = str(row['Student_Name'])
                
                raw_marks = row['Marks_Obtained']
                if isinstance(raw_marks, str):
                    marks = [float(m.strip()) for m in raw_marks.split(',') if m.strip()]
                else:
                    marks = [float(raw_marks)]

                if s_id in self.students:
                    self.students[s_id].get_marks().extend(marks)
                else:
                    self.students[s_id] = Student(s_id, name, marks)
            
            print(f"Successfully loaded {len(self.students)} student records from {self.filename}.")
        except Exception as e:
            print(f"Error reading CSV file: {e}")

    def save_to_csv(self):
        try:
            data = []
            for student in self.students.values():
                marks_val = ",".join(map(str, student.get_marks()))
                data.append({
                    'Student_ID': student.get_student_id(),
                    'Student_Name': student.get_name(),
                    'Marks_Obtained': marks_val
                })
            df = pd.DataFrame(data)
            df.to_csv(self.filename, index=False)
        except Exception as e:
            print(f"Error saving to CSV file: {e}")

    def add_student(self):
        print("\n--- Add New Student ---")
        s_id = input("Enter Student ID: ").strip()
        if s_id in self.students:
            print("Error: Student ID already exists!")
            return

        name = input("Enter Name: ").strip()
        
        try:
            marks_input = input("Enter Marks separated by space (e.g., 85 90 78): ")
            marks = [float(m) for m in marks_input.split()]
            
            if not all(0 <= m <= 100 for m in marks):
                print("Error: Marks must be between 0 and 100.")
                return

            new_student = Student(s_id, name, marks)
            self.students[s_id] = new_student
            self.save_to_csv()
            print("Student added and saved to CSV successfully!")
        except ValueError:
            print("Invalid input format. Please enter numeric values for marks.")

    def display_students(self):
        print("\n--- Student Records ---")
        if not self.students:
            print("No student records found.")
            return
        count = 0
        for student in self.students.values():
            student.display_details()
            count += 1
            if count >= 20 and len(self.students) > 20:
                print(f"... and {len(self.students) - 20} more students.")
                break

    def search_student(self):
        print("\n--- Search Student ---")
        s_id = input("Enter Student ID to search: ").strip()
        student = self.students.get(s_id)
        if student:
            student.display_details()
        else:
            print("Student not found.")

    def update_student(self):
        print("\n--- Update Student Records ---")
        s_id = input("Enter Student ID to update: ").strip()
        student = self.students.get(s_id)
        if not student:
            print("Student not found.")
            return

        print(f"Current Details: ", end="")
        student.display_details()

        name = input("Enter new Name (leave blank to keep current): ").strip()
        if name:
            student.set_name(name)

        try:
            marks_input = input("Enter new Marks separated by space (leave blank to keep current): ").strip()
            if marks_input:
                marks = [float(m) for m in marks_input.split()]
                if all(0 <= m <= 100 for m in marks):
                    student.set_marks(marks)
                else:
                    print("Invalid marks range. Marks not updated.")

            self.save_to_csv()
            print("Student record updated and saved to CSV successfully!")
        except ValueError:
            print("Invalid numeric input. Update failed.")

    def delete_student(self):
        print("\n--- Delete Student ---")
        s_id = input("Enter Student ID to delete: ").strip()
        if s_id in self.students:
            del self.students[s_id]
            self.save_to_csv()
            print("Student deleted and CSV updated successfully!")
        else:
            print("Student ID not found.")

    def calculate_average_marks(self):
        print("\n--- Calculate Class Average Marks ---")
        if not self.students:
            print("No student records available.")
            return
        
        total_avg = sum(s.calculate_average() for s in self.students.values())
        overall_avg = total_avg / len(self.students)
        print(f"Total Students: {len(self.students)}")
        print(f"Overall Class Average Score: {overall_avg:.2f}")


def main():
    manager = StudentManager("student_records_100.csv")

    while True:
        print("\n======================================")
        print(" STUDENT MANAGEMENT SYSTEM (CSV LINKED) ")
        print("======================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student Records")
        print("5. Delete Student")
        print("6. Calculate Class Average Marks")
        print("7. Save & Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.display_students()
        elif choice == '3':
            manager.search_student()
        elif choice == '4':
            manager.update_student()
        elif choice == '5':
            manager.delete_student()
        elif choice == '6':
            manager.calculate_average_marks()
        elif choice == '7':
            manager.save_to_csv()
            print("Changes saved to CSV. Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 7.")

if __name__ == "__main__":
    main()
