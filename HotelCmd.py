print("🏨 Welcome to the Hotel Management System!")

menu = {
    1: "View Rooms",
    2: "Book Room",
    3: "Book Food Item",
    4: "View Bookings",
    5: "Exit"
}

# Available Rooms
rooms = {
    "1 BHK": 5000,
    "2 BHK": 7000
}

# Food Menu
food_items = {
    "Veg Thali": 150,
    "Non-Veg Thali": 200,
    "Pizza": 250,
    "Burger": 100,
    "Sandwich": 80
}

room_bookings = []
food_bookings = []

while True:
    print("\n" + "=" * 40)
    print("           HOTEL MENU")
    print("=" * 40)

    for key, value in menu.items():
        print(f"{key}. {value}")

    try:
        choice = int(input("\nEnter your choice: "))

        # View Rooms
        if choice == 1:
            print("\n🏠 Available Rooms:")
            for room, price in rooms.items():
                print(f"{room} - ₹{price}")

        # Book Room
        elif choice == 2:
            print("\n🏠 Available Rooms:")
            room_list = list(rooms.keys())

            for i, room in enumerate(room_list, start=1):
                print(f"{i}. {room} - ₹{rooms[room]}")

            room_choice = int(input("Select Room: "))

            if 1 <= room_choice <= len(room_list):
                selected_room = room_list[room_choice - 1]
                name = input("Enter Customer Name: ")

                room_bookings.append({
                    "name": name,
                    "room": selected_room,
                    "price": rooms[selected_room]
                })

                print(f"✅ {selected_room} booked successfully for {name}")
            else:
                print("❌ Invalid Room Selection")

        # Book Food
        elif choice == 3:
            print("\n🍔 Food Menu:")

            food_list = list(food_items.keys())

            for i, food in enumerate(food_list, start=1):
                print(f"{i}. {food} - ₹{food_items[food]}")

            food_choice = int(input("Select Food Item: "))

            if 1 <= food_choice <= len(food_list):
                selected_food = food_list[food_choice - 1]
                qty = int(input("Enter Quantity: "))

                total = food_items[selected_food] * qty

                food_bookings.append({
                    "food": selected_food,
                    "qty": qty,
                    "total": total
                })

                print(f"✅ {selected_food} ordered successfully")
                print(f"💰 Total Bill: ₹{total}")
            else:
                print("❌ Invalid Food Selection")

        # View Bookings
        elif choice == 4:
            print("\n📋 ROOM BOOKINGS")

            if len(room_bookings) == 0:
                print("No Room Bookings Found")
            else:
                for booking in room_bookings:
                    print(
                        f"Customer: {booking['name']} | "
                        f"Room: {booking['room']} | "
                        f"Price: ₹{booking['price']}"
                    )

            print("\n🍔 FOOD BOOKINGS")

            if len(food_bookings) == 0:
                print("No Food Orders Found")
            else:
                for order in food_bookings:
                    print(
                        f"Food: {order['food']} | "
                        f"Qty: {order['qty']} | "
                        f"Bill: ₹{order['total']}"
                    )

        # Exit
        elif choice == 5:
            print("🙏 Thank You for Visiting!")
            break

        else:
            print("❌ Invalid Choice")

    except ValueError:
        print("❌ Please Enter Valid Number")