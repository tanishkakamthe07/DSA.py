import os

DATA_FILE = "records.txt"
INDEX_FILE = "index.txt"


def add_record(record_id, name, department):
    if search_index(record_id) is not None:
        print(f"Record with ID {record_id} already exists.")
        return

    with open(DATA_FILE, "a") as df:
        offset = df.tell()
        df.write(f"{record_id},{name},{department}\n")

    with open(INDEX_FILE, "a") as idx_f:
        idx_f.write(f"{record_id},{offset}\n")

    print(f"Record {record_id} added at byte offset {offset}.")


def search_index(target_id):
    if not os.path.exists(INDEX_FILE):
        return None

    with open(INDEX_FILE, "r") as idx_f:
        for line in idx_f:
            rec_id, offset = line.strip().split(",")
            if int(rec_id) == target_id:
                return int(offset)
    return None


def search_record(target_id):
    offset = search_index(target_id)
    if offset is None:
        print(f"Record ID {target_id} not found in index.")
        return

    with open(DATA_FILE, "r") as df:
        df.seek(offset)
        record = df.readline().strip()
        rec_id, name, dept = record.split(",")
        print(f"\n--- Record Found (Offset: {offset}) ---")
        print(f"ID: {rec_id} | Name: {name} | Department: {dept}")


def display_all():
    if not os.path.exists(DATA_FILE) or not os.path.exists(INDEX_FILE):
        print("No records found yet.")
        return

    print("\n--- Index File Contents (ID -> Byte Offset) ---")
    with open(INDEX_FILE, "r") as idx_f:
        for line in idx_f:
            rec_id, offset = line.strip().split(",")
            print(f"ID: {rec_id} -> Offset: {offset}")

    print("\n--- Data File Contents ---")
    with open(DATA_FILE, "r") as df:
        for line in df:
            print(line.strip())


if __name__ == "__main__":
    while True:
        print("\n1. Add Record\n2. Search Record by ID\n3. Display Index & Data Files\n4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            rec_id = int(input("Enter Record ID (integer): "))
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            add_record(rec_id, name, dept)
        elif choice == 2:
            rec_id = int(input("Enter Record ID to search: "))
            search_record(rec_id)
        elif choice == 3:
            display_all()
        elif choice == 4:
            break
        else:
            print("Invalid choice.")
