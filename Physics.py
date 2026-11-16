
# PHYSICS OPERATIONS USING FUNCTIONS

# Function to calculate Speed
def speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))

    if time != 0:
        print("Speed =", distance / time, "m/s")
    else:
        print("Time cannot be zero")


# Function to calculate Distance
def distance():
    speed_value = float(input("Enter speed (m/s): "))
    time = float(input("Enter time (s): "))

    print("Distance =", speed_value * time, "m")


# Function to calculate Time
def time_taken():
    distance_value = float(input("Enter distance (m): "))
    speed_value = float(input("Enter speed (m/s): "))

    if speed_value != 0:
        print("Time =", distance_value / speed_value, "s")
    else:
        print("Speed cannot be zero")


# Function to calculate Force
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))

    print("Force =", mass * acceleration, "N")


# Function to calculate Work
def work():
    force_value = float(input("Enter force (N): "))
    distance_value = float(input("Enter distance (m): "))

    print("Work =", force_value * distance_value, "J")


# Function to calculate Power
def power():
    work_done = float(input("Enter work done (J): "))
    time_value = float(input("Enter time (s): "))

    if time_value != 0:
        print("Power =", work_done / time_value, "W")
    else:
        print("Time cannot be zero")


# Function to calculate Pressure
def pressure():
    force_value = float(input("Enter force (N): "))
    area = float(input("Enter area (m²): "))

    if area != 0:
        print("Pressure =", force_value / area, "Pa")
    else:
        print("Area cannot be zero")


# Function to calculate Density
def density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m³): "))

    if volume != 0:
        print("Density =", mass / volume, "kg/m³")
    else:
        print("Volume cannot be zero")


# Main program using while loop
while True:

    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Speed")
    print("2. Distance")
    print("3. Time")
    print("4. Force")
    print("5. Work")
    print("6. Power")
    print("7. Pressure")
    print("8. Density")

    choice = input("Choose a physics operation (1-8): ")

    if choice == "1":
        speed()

    elif choice == "2":
        distance()

    elif choice == "3":
        time_taken()

    elif choice == "4":
        force()

    elif choice == "5":
        work()

    elif choice == "6":
        power()

    elif choice == "7":
        pressure()

    elif choice == "8":
        density()

    else:
        print("Invalid choice!")

    # Ask user whether to continue
    answer = input("\nDo you want to continue? (yes/no): ")

    if answer.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break
