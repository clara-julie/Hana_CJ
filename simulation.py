import numpy as np

def simulate_wealth(age_shares, medians, percentile_values=None, seed=42):
    """
    Simulate wealth for 10,000 adults.

    Parameters
    ----------
    age_shares : array
        Population shares of the eight age groups.
    medians : array
        Median wealth (P50) for each age group.
    percentile_values : array, optional
        Wealth percentiles P1-P99 for each age group.
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    age : array
        Simulated age group indices.
    wealth : array
        Simulated net wealth for each adult.
    """

    rng = np.random.default_rng(seed)
    n = 10000

    # Drawing a random number between 0 and 1 for each adult
    u = rng.uniform(0, 1, size=n)

    # Assigning adults to age groups based on population shares
    age = np.zeros(n, dtype=int)
    lower = 0

    for j, share in enumerate(age_shares):
        upper = lower + share
        mask = (u >= lower) & (u < upper)
        age[mask] = j
        lower = upper

    # Giving each adult the median wealth of their age group
    wealth = np.asarray(medians)[age].copy()

    # Allowing wealth to vary within age groups (Part 2.2)
    if percentile_values is not None:
        ranks = rng.integers(1, 100, size=n)

        for i in range(n):
            wealth[i] = percentile_values[age[i], ranks[i] - 1]

    return age, wealth