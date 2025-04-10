import numpy as np
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore
# from sklearn.metrics import accuracy_score
# from rich import print
from rich.console import Console

console = Console()
console.clear()
print = console.print

print('Play with numpy')

a_np_array, a_range = np.arange(10), range(5)
print(f'{a_np_array=}')
print(f'{list(a_range)=}')

# Create a 2D array
converted_array = a_np_array.reshape(5,2)
print(f'{converted_array=}')
print(f'{converted_array.shape=}')
print(f'{converted_array.ndim=}')
print(f'{converted_array.size=}')
print(f'{len(converted_array)=}')

# Split
X_train, X_test, y_train, y_test = train_test_split(converted_array, list(a_range),
                                                    test_size=0.33,
                                                    random_state=42)
print(f'{X_train=}')
print(f'{X_test=}')
print(f'{y_train=}')
print(f'{y_test=}')

k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

distances, indices = knn.kneighbors(X_test)
print(f'{distances=}')
print(f'{indices=}')

y_pred = knn.predict(X_test)
print(f'{y_pred=}')



