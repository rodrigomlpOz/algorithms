def findMinArrowShots(points):
    # If there are no balloons, return 0
    if not points:
        return 0
    
    # Sort balloons by their end point
    points.sort(key=lambda x: x[1])
    
    # Initialize the number of arrows and the first arrow position
    arrows = 1
    current_arrow_position = points[0][1]
    
    # Iterate through the balloons
    for i in range(1, len(points)):
        # If the current balloon starts after the current arrow position
        # shoot a new arrow and update the arrow position
        if points[i][0] > current_arrow_position:
            arrows += 1
            current_arrow_position = points[i][1]
    
    return arrows