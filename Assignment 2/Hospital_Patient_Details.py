patients: list[dict] = [
    {"id": 1, "patient_name": "Walter White", "age": 50, "gender": "Male",
     "disease": "Diabetes", "doctor": "Dr. Kumar", "bill": 5000},

    {"id": 2, "patient_name": "Jesse Pinkman", "age": 27, "gender": "Male",
     "disease": "Asthma", "doctor": "Dr. Ravi", "bill": 3000},

    {"id": 3, "patient_name": "Skyler White", "age": 40, "gender": "Female",
     "disease": "Migraine", "doctor": "Dr. Priya", "bill": 2500},

    {"id": 4, "patient_name": "Hank Schrader", "age": 43, "gender": "Male",
     "disease": "Blood Pressure", "doctor": "Dr. Suresh", "bill": 4500},

    {"id": 5, "patient_name": "Marie Schrader", "age": 42, "gender": "Female",
     "disease": "Anemia", "doctor": "Dr. Priya", "bill": 3500},

    {"id": 6, "patient_name": "Saul Goodman", "age": 45, "gender": "Male",
     "disease": "Back Pain", "doctor": "Dr. Kumar", "bill": 4000},

    {"id": 7, "patient_name": "Kim Wexler", "age": 38, "gender": "Female",
     "disease": "Fever", "doctor": "Dr. Ravi", "bill": 2000},

    {"id": 8, "patient_name": "Mike Ehrmantraut", "age": 65, "gender": "Male",
     "disease": "Heart Disease", "doctor": "Dr. Suresh", "bill": 12000},

    {"id": 9, "patient_name": "Gustavo Fring", "age": 50, "gender": "Male",
     "disease": "Blood Pressure", "doctor": "Dr. Kumar", "bill": 6000},

    {"id": 10, "patient_name": "Nacho Varga", "age": 35, "gender": "Male",
     "disease": "Kidney Stone", "doctor": "Dr. Ravi", "bill": 8000}
]

def add_patient(patients: list[dict]) -> None:
    patient_name: str = input("Enter Patient Name: ")
    age: int = int(input("Enter Age: "))
    gender: str = input("Enter Gender: ")
    disease: str = input("Enter Disease: ")
    doctor: str = input("Enter Doctor: ")
    bill: float = float(input("Enter Bill: "))

    patient: dict = {
        "id": len(patients) + 1,
        "patient_name": patient_name,
        "age": age,
        "gender": gender,
        "disease": disease,
        "doctor": doctor,
        "bill": bill
    }
    patients.append(patient)

    print("Patient added")


def view_patients(patients: list[dict]) -> None:
    for index, patient in enumerate(patients, start=1):
        print(
            index,
            patient["patient_name"],
            "| Age:", patient["age"],
            "| Disease:", patient["disease"],
            "| Doctor:", patient["doctor"],
            "| Bill:", patient["bill"]
        )

def search_patient(patients: list[dict]) -> None:
    patient_name: str = input("Enter patient name: ")

    found: bool = any(patient["patient_name"].lower() == patient_name.lower() for patient in patients)

    for patient in patients:

        if patient["patient_name"].lower() == patient_name.lower():
            print("Patient Found")
            print("ID:", patient["id"])
            print("Name:", patient["patient_name"])
            print("Age:", patient["age"])
            print("Disease:", patient["disease"])
            print("Doctor:", patient["doctor"])
            print("Bill:", patient["bill"])

            break

    if not found:
        print("Patient not found")


def find_by_doctor(patients: list[dict]) -> None:

    doctor: str = input("Enter doctor name: ")

    def is_doctor(patient: dict) -> bool:
        return patient["doctor"].lower() == doctor.lower()

    found: bool = False

    for patient in patients:

        if is_doctor(patient):
            print(patient["patient_name"], "-", patient["doctor"])
            found = True

    if not found:
        print("No patients found for this doctor")


def sort_by_age(patients: list[dict]) -> None:

    sorted_patients: list[dict] = sorted(patients,key=lambda patient: patient["age"])

    for index, patient in enumerate(sorted_patients, start=1):
        print(index,patient["patient_name"],"-", patient["age"])


while True:

    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Find Patients by Doctor")
    print("5. Sort Patients by Age")
    print("6. Exit")

    choice: int = int(input("Enter your choice: "))

    match choice:

        case 1:
            add_patient(patients)

        case 2:
            view_patients(patients)

        case 3:
            search_patient(patients)

        case 4:
            find_by_doctor(patients)

        case 5:
            sort_by_age(patients)

        case 6:
            print("Exited")
            break

        case _:
            print("Invalid choice")