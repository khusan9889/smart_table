import time

current_distance = 0
def up_table(height_cm):
    global current_distance  # Use the global variable to update current_distance
    height_cm = int(height_cm)
    print("Increase to:", height_cm)

    # Calculate the target height
    target_height = current_distance + height_cm
    print(f"Raising table to {target_height} cm")

    # Check if the target height is less than the current height
    if target_height < current_distance:
        print("Error: Target height is lower than the current height.")
        return

    # Calculate the height difference
    height_difference = target_height - current_distance

    # Calculate the time required to raise the table to the target height
    time_to_raise_factor = 0.5  # Adjust this factor as needed
    time_to_raise = height_difference * time_to_raise_factor

    # Raise the table
    # GPIO.output(11, 0)
    time.sleep(time_to_raise)
    # GPIO.output(11, 1)
    print(f"Table is raised to {target_height} cm")


def down_table(height_cm):
    global current_distance
    height_cm = int(height_cm)
    print("Decrease by:", height_cm)

    # Calculate the target height
    target_height = current_distance - height_cm
    print(f"Lowering table to {target_height} cm")

    # Check if the target height is greater than the current height
    # if target_height > current_distance:
    # print("Error: Target height is higher than the current height.")
    # return

    # Calculate the height difference
    height_difference = target_height - current_distance

    # Calculate the time required to lower the table to the target height
    time_to_lower_factor = 0.5  # Adjust this factor as needed
    time_to_lower = height_difference * time_to_lower_factor

    # GPIO.output(13, 0)
    time.sleep(time_to_lower)
    # GPIO.output(13, 1)
    current_distance = target_height  # Update the current distance
    print(f"Table is lowered to {target_height} cm")


def bind_button():
    print("Binding button")
    # press save button and off
    # GPIO.output(15, 0)
    # GPIO.output(15, 1)
