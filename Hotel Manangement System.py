## HOTEL MANAGEMENT SYSTEM 
## BY HARSH P. S. PARIHAR


from datetime import datetime

class Hotel:
    def __init__(self):
        self.guests = []

    def add_guest(self):
        name = input("Enter guest name: ")
        age = int(input("Enter guest age: "))
        address = input("Enter guest address: ")
        room_number = int(input("Enter room number: "))
        room_type = input("Enter room type (AC/Non-AC): ")
        bed_type = input("Enter bed type (Single bed/Double bed): ")
        guest_type = input("Enter guest type (Individual/Family): ")
        check_in_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        guest = {
            'name': name,
            'age': age,
            'address': address,
            'room_number': room_number,
            'room_type': room_type,
            'bed_type': bed_type,
            'guest_type': guest_type,
            'check_in_time': check_in_time,
            'check_out_time': None
        }
        self.guests.append(guest)
        print(f"Room {room_number} {room_type} {bed_type} is provided to {name}")

    def check_out_guest(self):
        room_number = int(input("Enter room number for check-out: "))
        check_out_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for guest in self.guests:
            if guest['room_number'] == room_number:
                guest['check_out_time'] = check_out_time
                print(f"Guest {guest['name']} checked out from room {room_number} at {check_out_time}.")
                return
        print(f"No guest found in room {room_number}.")

    def view_guests(self):
        if not self.guests:
            print("No guests currently in the hotel.")
        else:
            print("Current guests in the hotel:")
            for guest in self.guests:
                print(f"Name: {guest['name']}, Age: {guest['age']}, Address: {guest['address']}, "
                      f"Room Number: {guest['room_number']}, Room Type: {guest['room_type']}, "
                      f"Bed Type: {guest['bed_type']}, Guest Type: {guest['guest_type']}, "
                      f"Check-In Time: {guest['check_in_time']}, Check-Out Time: {guest['check_out_time']}")

    def guests_status(self):
        if not self.guests:
            print("No guests currently in the hotel.")
        else:
            print("Defining all guests in the hotel:")
            for guest in self.guests:
                print(f"Guest {guest['name']} (Age: {guest['age']}, Address: {guest['address']}) is staying in room "
                      f"{guest['room_number']} with a {guest['room_type']} room and {guest['bed_type']} bed for "
                      f"{guest['guest_type']}. Check-In Time: {guest['check_in_time']}, "
                      f"Check-Out Time: {guest['check_out_time']}")

# Example usage
hotel = Hotel()

while True:
    print("\nHotel Management System")
    print("1. Add Guest")
    print("2. Check Out Guest")
    print("3. View Guests")
    print("4. Guests Status")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        hotel.add_guest()
    elif choice == 2:
        hotel.check_out_guest()
    elif choice == 3:
        hotel.view_guests()
    elif choice == 4:
        hotel.guests_status()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
