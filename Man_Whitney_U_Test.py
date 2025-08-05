from scipy.stats import mannwhitneyu

m = [0, 0, 12.6, 7.3, 3.6, 0, 0, 0, 0, 0, 0]
f = [7.6, 15.6, 14.4, 0, 0, 0]

stat, p = mannwhitneyu(m, f, alternative='two-sided')

print("U-Statistik:", stat)
print("p-Wert:", p)
