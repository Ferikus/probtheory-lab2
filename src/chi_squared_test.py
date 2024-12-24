import numpy as np
import scipy.stats as st

def calculate_interval_probabilities(intervals, mean, variance):
    probabilities = []

    for i in range(len(intervals) - 1):
        lower_bound = intervals[i]
        upper_bound = intervals[i + 1]

        prob_upper = st.norm.cdf(upper_bound, loc=mean, scale=np.sqrt(variance))
        prob_lower = st.norm.cdf(lower_bound, loc=mean, scale=np.sqrt(variance))

        # вероятность попасть в текущий интервал
        interval_probability = prob_upper - prob_lower

        probabilities.append(interval_probability)

    return np.array(probabilities)

def chi_squared_test(intervals_num, sample_array, mean, variance, alpha):
    sample_size = len(sample_array)
    std_dev = np.sqrt(variance)
    ppf = np.linspace(0, 1, intervals_num + 1)
    intervals = st.norm.ppf(ppf, mean, std_dev)

    hist_values, _ = np.histogram(sample_array, bins=intervals)

    # получаем квантили
    interval_probabilities = calculate_interval_probabilities(intervals, mean, variance)

    # статистика критерия - R0
    chi2_stat = np.sum(((hist_values - sample_size * interval_probabilities) ** 2) / (sample_size * interval_probabilities))
    chi_distribution = st.chi2.cdf(chi2_stat, intervals_num - 1)
    f_value = 1 - chi_distribution

    # решение об отклонении гипотезы
    if f_value <= alpha:
        output = "Гипотеза отклоняется"
    else:
        output = "Гипотеза не отклоняется"

    return interval_probabilities, chi2_stat, f_value, output