# -*- coding: utf-8 -*-
"""Project_Phase2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yg4hsSGBaiEWRtWx-cCE63vQHd9iiftb

Upload the Dataset
"""

from google.colab import files
uploaded=files.upload()

"""Load the Dataset"""

import tensorflow as tf
from tensorflow.keras import datasets

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Normalize the pixel values to a range of 0 to 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Display the shape of the data
print("Training data shape:", train_images.shape)
print("Test data shape:", test_images.shape)

# You can also check one sample to visualize an image
import matplotlib.pyplot as plt

# Display the first training image
plt.imshow(train_images[0], cmap=plt.cm.binary)
plt.title(f"Label: {train_labels[0]}")
plt.show()

"""Data Exploration"""

#display first few roes
df.head()

#Shape of the dataset
print("shape:",df.shape)
#column names
print("column:",df.columns.tolist())
#Data types and non-null values
df.info()
#summary statistics for numeric features
df.describe()

"""Check for Missing Values and Duplicates"""

#check for missing values
print (df.isnull().sum())
#check for duplicates
print("Duplicate rows:",df.duplicated().sum())

"""Visualize a Few Features"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# Load dataset
digits = load_digits()
X = digits.data
y = digits.target

# Reduce dimensions to 2D with PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot the digits in 2D PCA space
plt.figure(figsize=(10, 7))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10', alpha=0.7)
plt.colorbar(scatter, label='Digit Label')
plt.title('MNIST Digits Visualized in 2D using PCA')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)
plt.show()

"""Identify Target and Features"""

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
digits = load_digits()
X, y = digits.data, digits.target  # Features and Target

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

"""Convert Categorical Columns to Numerical"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Example dataset with categorical digit labels
data = pd.DataFrame({
    'pixel1': [0, 128, 255],
    'pixel2': [255, 128, 0],
    'digit_label': ['zero', 'one', 'two']  # Categorical
})

# Convert categorical labels to numeric
label_encoder = LabelEncoder()
data['digit_label_encoded'] = label_encoder.fit_transform(data['digit_label'])

print(data)

"""
One-Hot Encoding"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Normalize the images to a range of [0, 1]
train_images, test_images = train_images / 255.0, test_images / 255.0

# One-Hot Encode the labels
train_labels_one_hot = to_categorical(train_labels)
test_labels_one_hot = to_categorical(test_labels)

# Define a simple CNN model for digit classification
model = models.Sequential([
    layers.Reshape((28, 28, 1), input_shape=(28, 28)),  # Reshape input to 28x28x1 for CNN
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 output neurons for digits 0-9
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels_one_hot, epochs=5, batch_size=64)

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels_one_hot)

print(f"Test accuracy: {test_acc * 100:.2f}%")

# Visualize some of the predictions
predictions = model.predict(test_images)

# Show the first 5 test images and their predicted labels
for i in range(5):
    plt.imshow(test_images[i], cmap='gray')
    plt.title(f"Predicted: {np.argmax(predictions[i])}, Actual: {test_labels[i]}")
    plt.show()

"""Feature Scaling"""

import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

# Load the dataset
digits = load_digits()
data = digits.data
target = digits.target

# Initialize MinMaxScaler (scales features to the range [0, 1])
scaler = MinMaxScaler()

# Apply scaling to the features
scaled_data = scaler.fit_transform(data)

# Let's check the first image's scaled data
plt.imshow(scaled_data[0].reshape(8, 8), cmap='gray')
plt.title(f"Digit: {target[0]}")
plt.show()

"""Train-Test Split"""

# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the MNIST dataset
mnist = fetch_openml('mnist_784')

# Separate the features (X) and labels (y)
X = mnist.data
y = mnist.target

# Train-test split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data (Standardize)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_scaled, y_train)

# Make predictions and evaluate the model
y_pred = clf.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

# Output the accuracy
print(f"Accuracy: {accuracy * 100:.2f}%")

"""Model Building"""

# Importing necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
digits = datasets.load_digits()
X = digits.data
y = digits.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and train the Support Vector Machine classifier
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

"""Evaluation"""

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the MNIST dataset
digits = datasets.load_digits()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3, random_state=42)

# Standardize the dataset (scaling features)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train the KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Evaluate the classifier's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

"""Make Predictions from New Input"""

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Load the digits dataset
digits = datasets.load_digits()
X = digits.images  # image data (8x8 pixel images)
y = digits.target  # target labels (0-9)

# Flatten the images to 1D arrays (8x8 = 64 pixels)
n_samples = len(X)
X_flat = X.reshape((n_samples, -1))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_flat, y, test_size=0.5, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Test the classifier
y_pred = clf.predict(X_test)

# Print classification report
print(classification_report(y_test, y_pred))

# Plot a sample image and the predicted label
plt.imshow(X_test[0].reshape(8, 8), cmap='gray')
plt.title(f"Predicted Label: {y_pred[0]}")
plt.show()

"""Convert to DataFrame and Encode"""

import pandas as pd
from sklearn.datasets import load_digits
from sklearn.preprocessing import LabelEncoder

# Load handwritten digits dataset
digits = load_digits()

# Convert to DataFrame
df = pd.DataFrame(digits.data)
df['label'] = digits.target

# Encode the label column (optional here as it's already numeric)
encoder = LabelEncoder()
df['encoded_label'] = encoder.fit_transform(df['label'])

print(df.head())

"""Predict the Final Grade"""

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)

# Train model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Final Grade (Accuracy):", round(accuracy * 100, 2), "%")

"""Deployment-Building an Interactive App"""

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize the images
train_images = train_images / 255.0
test_images = test_images / 255.0

# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5)

# Save the model
model.save('digit_recognition_model.h5')

"""Create a Prediction Function"""

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile and train
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

# Prediction function
def predict_digit(image):
    image = image.reshape(1, 28, 28) / 255.0  # Preprocess image
    prediction = model.predict(image)
    return np.argmax(prediction)

# Example usage
index = 0  # Change index to test other images
sample_image = x_test[index]
predicted = predict_digit(sample_image)

plt.imshow(sample_image, cmap='gray')
plt.title(f"Predicted Digit: {predicted}")
plt.axis('off')
plt.show()