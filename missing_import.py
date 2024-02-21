"""
This code will intentionally raise a NameError because the numpy module is not
installed. It's used to create an error in the GitHub Actions Pipeline.
"""

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

result = np.add(vector1, vector2)