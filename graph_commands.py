# %%
import matplotlib.pyplot as plt
import seaborn as sns

results = [[1229,  320],[ 176,  385]]

# %% Plot confusion matrix
plt.figure(figsize=(8,6))
sns.heatmap(results, annot=True, fmt='g', cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Exibindo o classification report
# %%
days = 	[2.0, 22.0, 6.0, 14.0, 15.0, 20.0, 24.0, 21.0, 27.0, 27.0, 27.0, 1.0, 4.0, 8.0, 13.0]
sns.distplot(days, kde=False, bins=31)

# %%
