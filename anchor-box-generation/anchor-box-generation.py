def generate_anchors(
    feature_size: int,
    image_size: float,
    scales: list[float],
    aspect_ratios: list[float]
) -> list[list[float]]:

    stride = image_size / feature_size

    final_array = []

    for i in range(feature_size):
        for j in range(feature_size):

            c_x = (j + 0.5) * stride
            c_y = (i + 0.5) * stride

            for scale in scales:
                for aspect_ratio in aspect_ratios:

                    width = scale * (aspect_ratio ** 0.5)
                    height = scale / (aspect_ratio ** 0.5)

                    x1 = c_x - width / 2
                    y1 = c_y - height / 2
                    x2 = c_x + width / 2
                    y2 = c_y + height / 2

                    final_array.append([x1, y1, x2, y2])

    return final_array