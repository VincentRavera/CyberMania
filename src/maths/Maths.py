def update_position_of_object(my_object):
    """
    Update the position of an object
    """
    speed = my_object.speed
    current_position = my_object.position
    new_position = current_position + speed
    my_object.position = new_position
