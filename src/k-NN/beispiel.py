from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Laden des Iris-Datensatzes
iris = load_iris()
# Aufteilen des Datensatzes in Features (X) und Labels (y)
# Labels können sein: 0 für Setosa, 1 für Versicolor und 2 für Virginica
features = iris.data
labels = iris.target

# Aufteilen des Datensatzes in Trainings- und Testdaten
# 70% der Daten werden für das Training verwendet, 30% für das Testen
# Der random_state wird auf 42 gesetzt, damit die Aufteilung reproduzierbar ist
feature_training, feature_test, label_training, label_test = train_test_split(features, labels, 
                                                    test_size=0.3, 
                                                    random_state=42)

# Erstellen und Trainieren des k-NN-Klassifikators
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(feature_training, label_training)

# Vorhersagen auf den Testdaten
y_pred = knn.predict(feature_test)

# Berechnen der Genauigkeit
accuracy = accuracy_score(label_test, y_pred)
print(f"Genauigkeit: {accuracy:.2f}")