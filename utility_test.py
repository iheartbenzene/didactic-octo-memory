import numpy as np

# from tensorflow.python.keras.models import Sequential
# from tensorflow.python.keras.layers import BatchNormalization, Dense, Flatten, Input, LeakyReLU, Reshape

from keras.models import Sequential, Model
from keras.layers import BatchNormalization, Dense, Flatten, Input, LeakyReLU, Reshape
from keras.optimizers import Adam
from keras.datasets import mnist

class GAN():
    def __init__(self):
        self.image_rows = 28
        self.image_cols = 28
        self.channels = 1
        self.image_shape = (self.image_rows, self.image_cols, self.channels)
        
        optimizer = Adam(0.0002, 0.5)
        
        self.discriminator = self.building_discriminator()
        self.discriminator.compile(loss='binary_crossentropy', optimizer=optimizer,
                                   metrics=['accuracy'])
        
        self.generator = self.building_generator()
        self.generator.compile(loss='binary_crossentropy', optimizer=optimizer)
        
        input_shape = Input(shape=(100, ))
        image = self.generator(input_shape)
        
        self.discriminator.trainale = False
        
        validate = self.discriminator(image)
        
        self.combined = Model(input_shape, validate)
        self.combined.compile(loss='binary_crossentropy', optimizer=optimizer)
        
    def building_generator(self):
        noisiness = (100, )
        model = Sequential()
        model.add(Dense(256, input_shape = noisiness))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(512))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(1024))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(np.prod(self.image_shape), activation='tanh'))
        model.add(Reshape(self.image_shape))
        
        model.summary()
        
        noise = Input(shape=noisiness)
        image = model(noise)
        
        return Model(noise, image)
    
    def building_discriminator(self):
        image_shape = (self.image_rows, self.image_cols, self.channels)
        
        model = Sequential()
        model.add(Flatten(input_shape=image_shape))
        model.add(Dense(512))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(256))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(1, activation='sigmoid'))
        model.summary()
        
        image = Input(shape=image_shape)
        validity = model(image)
        
        return Model(image, validity)
    
    def training(self, epochs, batch_size=128, save_interval=50):
        
        (train_x, _), (_, _) = mnist.load_data()
        
        train_x = (train_x.astype(np.float32) - 127.5) / 127.5
        train_x = np.expand_dims(train_x, axis=3)
        
        half_batch = int(batch_size/2)
        
        for epoch in range(epochs):
            index = np.random.randint(0, train_x.shape[0], half_batch)
            images = train_x[index]
            
            noise = np.random.normal(0, 1, (half_batch, 100))
            
            generate_imates = self.generator.predict(noise)
            
            discriminator_loss_real = self.discriminator.train_on_batch(images, np.ones((half_batch, 1)))
            discriminator_loss_imaginary = self.discriminator.train_on_batch(generate_imates, np.zeros((half_batch, 1)))
            discriminator_loss = 0.5 * np.add(discriminator_loss_real, discriminator_loss_imaginary)
            
            noise = np.random.normal(0, 1, (batch_size, 100))
            
            validate_y = np.array([1] * batch_size)
            
            generator_loss = self.combined.train_on_batch(noise, validate_y)
            
            print("%d [Discriminator loss: %0.4f, accuracy: %0.4f] [Generator loss: %0.4f]" % (epoch, discriminator_loss[0], 100 * discriminator_loss[1], generator_loss))