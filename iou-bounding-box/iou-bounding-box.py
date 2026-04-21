def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    
    max_x1 = max(box_a[0], box_b[0])
    max_y1 = max(box_a[1], box_b[1])
    min_x2 = min(box_a[2], box_b[2])
    min_y2 = min(box_a[3], box_b[3])

    height_intersection = max(0, min_y2 - max_y1)
    width_intersection = max(0, min_x2 - max_x1)

    width_a = box_a[2] - box_a[0]
    height_a = box_a[3] - box_a[1]
    width_b = box_b[2] - box_b[0]
    height_b = box_b[3] - box_b[1]
    area_a = width_a * height_a
    area_b = width_b * height_b
    area_intersection = height_intersection * width_intersection
    area_union = area_a + area_b - area_intersection
    return area_intersection/area_union
    
    