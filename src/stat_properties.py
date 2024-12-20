def get_mean_sample(draw):
    return sum(draw) / len(draw)


def get_variance_sample(draw):
    mean_sample = get_mean_sample(draw)
    return sum([(x - mean_sample) ** 2 for x in draw]) / len(draw)


def get_median(draw):
    draw_len = len(draw)
    if draw_len % 2 == 0:
        median = (draw[draw_len // 2 - 1] + draw[draw_len // 2]) / 2
    else:
        median = draw[draw_len // 2]
    return median


def get_range_val(draw):
    return draw[-1] - draw[0]
