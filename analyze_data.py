import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

file_path = 'contact-lenses.xlsx'
df = pd.read_excel(file_path)
df_encoded = pd.get_dummies(df, drop_first=True)

# Feature selection for simpler tree
X = df_encoded[['tear-prod-rate_reduced', 'age_young']]
y = df_encoded['contact-lenses_none']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the decision tree with limited depth
clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X_train, y_train)

# Larger plot for better visualization
plt.figure(figsize=(20, 15))
plot_tree(clf, feature_names=X.columns, class_names=['None', 'Soft', 'Hard'], filled=True)
plt.show()
