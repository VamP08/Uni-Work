# Import necessary libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Step 1: Load and Preprocess the Data
# The MNIST dataset comes pre-packaged in Keras, containing 60,000 training images and 10,000 testing images.
# The images are grayscale (1 channel), 28x28 pixel images of handwritten digits (0-9).

# Load MNIST dataset - the dataset is split into training and testing sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Step 2: Data Normalization
# Normalize the pixel values to be between 0 and 1, as neural networks tend to perform better
# when input values are in this range (as opposed to 0-255).
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Step 3: Reshape the Data
# For fully connected networks, we flatten the 28x28 images into a 784-dimensional vector.
# However, for CNNs (Convolutional Neural Networks), we keep the 2D structure with a single channel.
x_train = np.expand_dims(x_train, -1)  # Shape: (60000, 28, 28, 1)
x_test = np.expand_dims(x_test, -1)    # Shape: (10000, 28, 28, 1)

# Step 4: One-Hot Encoding of Labels
# The labels are integers between 0-9, representing the digit classes.
# One-hot encoding transforms the labels into a binary matrix of shape (num_samples, num_classes).
y_train = to_categorical(y_train, 10)  # Shape: (60000, 10)
y_test = to_categorical(y_test, 10)    # Shape: (10000, 10)

# Step 5: Build the Model
# We'll use a simple CNN architecture with Conv2D, MaxPooling, and Dense layers.
model = models.Sequential()

# First convolutional layer: 32 filters, 3x3 kernel, ReLU activation, input shape is 28x28 with 1 channel
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))  # MaxPooling reduces dimensionality, making the model faster and less prone to overfitting.

# Second convolutional layer: 64 filters, 3x3 kernel, followed by another MaxPooling layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Third convolutional layer: 64 filters, 3x3 kernel
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Step 6: Flatten the 3D output to 1D to connect to a fully connected Dense layer
model.add(layers.Flatten())

# Fully connected Dense layer with 64 units and ReLU activation
model.add(layers.Dense(64, activation='relu'))

# Output layer with 10 units (one for each digit class) and softmax activation
# Softmax turns the output into probabilities for each class (summing to 1)
model.add(layers.Dense(10, activation='softmax'))

# Step 7: Compile the Model
# We compile the model by specifying:
# - The optimizer: 'adam' is an adaptive learning rate optimizer.
# - Loss function: 'categorical_crossentropy' is used for multiclass classification problems.
# - Metrics: We use 'accuracy' to measure the percentage of correct predictions.
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Step 8: Train the Model
# We train the model using the training data, with a batch size of 64 images, over 5 epochs.
# Validation data is used to check the model's performance after each epoch.
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))

# Step 9: Evaluate the Model
# After training, we evaluate the model's performance on the test data.
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc:.4f}')

# Step 10: Make Predictions
# Let's use the trained model to make predictions on the test set.
predictions = model.predict(x_test)

# Print the predicted class for the first test image (by taking the index of the highest probability)
print(f'Predicted class for the first test image: {np.argmax(predictions[0])}')

# Compare with the actual class
print(f'Actual class for the first test image: {np.argmax(y_test[0])}')

