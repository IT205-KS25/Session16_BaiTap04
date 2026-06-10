from datetime import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]


def find_patient_index(records, patient_id):
    patient_id = patient_id.strip().upper()

    for index, record in enumerate(records):
        data = record.split("-")

        if data[0] == patient_id:
            return index

    return -1


def display_records(records):
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")

    for index, record in enumerate(records, start=1):
        patient_id, name, birth_year, diagnosis = record.split("-")

        print(
            f"{index}. [{patient_id}] {name:<18} | Năm sinh: {birth_year} | Chẩn đoán: {diagnosis}"
        )

    print("--------------------------------------------------------------------------")


def add_patient(records):
    print("--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if patient_id == "":
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(records, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip()

    if name == "":
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        birth_year = input("Nhập năm sinh: ").strip()

        current_year = datetime.now().year

        if birth_year.isdigit() and 1900 <= int(birth_year) <= current_year:
            break

        print("Năm sinh không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán: ").strip()

    if diagnosis == "":
        print("Chẩn đoán không được để trống!")
        return

    name = name.replace("-", " ").title()
    diagnosis = diagnosis.replace("-", " ").capitalize()

    record = "-".join([
        patient_id,
        name,
        birth_year,
        diagnosis
    ])

    records.append(record)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print(record)


def update_diagnosis(records):
    print("--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    data = records[index].split("-")

    print(f"\nTìm thấy bệnh nhân: {data[1]}")
    print(f"Chẩn đoán hiện tại: {data[3]}")

    diagnosis = input("Nhập chẩn đoán mới: ").strip()

    if diagnosis == "":
        print("Chẩn đoán không được để trống!")
        return

    diagnosis = diagnosis.replace("-", " ").capitalize()

    data[3] = diagnosis

    records[index] = "-".join(data)

    print("\nCập nhật chẩn đoán thành công!")
    print("Dữ liệu mới được lưu:")
    print(records[index])


def generate_age_report(records):
    current_year = datetime.now().year

    children = 0
    adults = 0
    elderly = 0

    for record in records:
        birth_year = int(record.split("-")[2])

        age = current_year - birth_year

        if age < 16:
            children += 1
        elif age <= 60:
            adults += 1
        else:
            elderly += 1

    print("--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adults} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


while True:
    print()
    print("===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("==================================================")

    choice = input("Chọn chức năng (1-5): ")

    match choice:
        case "1":
            display_records(patient_records)

        case "2":
            add_patient(patient_records)

        case "3":
            update_diagnosis(patient_records)

        case "4":
            generate_age_report(patient_records)

        case "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-5!")