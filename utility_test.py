class GAN():
    def __init__(self):
        self.image_rows = 28
        self.image_cols = 28
        self.channels = 1
        self.image_shape = (self.image_rows, self.image_cols, self.channels)
        
        optimizer = Adam(0.0002, 0.5)
        
        self.discriminator = self.build_discriminator()
        self.discriminator.compile(loss='binary_crossentropy', optimizer=optimizer,
                                   metrics=['accuracy'])
        
        self.generator = self.build_generator()
        self.generator.compile(loss='binary_crossentropy', optimizer=optimizer)
        
        input_shape = Input(shape=(100, ))
        image = self.generator(input_shape)
        
        self.discriminator.trainale = False
        
        validate = self.discriminator(image)
        
        self.combined = Model(input_shape, validate)
        self.combined.compile(loss='binary_crossentropy', optimizer=optimizer)
        
    def build_generator(self):
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
    
    def build_discriminator(self):
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
        pass