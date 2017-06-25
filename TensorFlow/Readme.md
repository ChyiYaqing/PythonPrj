Popular machine Leanring Library 
    Google Tensorflow: 
        1. build a classifer that can look at image of handwritten character image classifier in 40 line, Tensorflow built to scale it was made to run on multiple CPU or GPU
            Install TensorFlow via pip(Package Manager By Python): with Virtualenv
                $ sudo easy_install pip 
                $ sudo easy_install -- upgrade pip 
                $ sudo pip install --upgrade virtualenv 
                $ virtualenv --system-site-packages -p python3 ~/tensorflow # for python3 
                $ source ~/tensorflow/bin/activate 
                $ pip3 install --upgrade tensorflow 
                $ pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.2.0-py3-none-any.whl # for example, if you are installing Tensorflow for Mac OS X, Python3.6, CPU 
                $ source ~/tensorflow/bin/activate 
                $ deactivate # deactivate the environment 
                $ rm -r ~/tensorflow # uninstalling Tensorflow OR $ pip uninstall tensorflow  
        2. TensorFlow provides a utility called TensorBoard that can display a picture of the computational graph. 
        3. placeholder -- is a promise to privide a value later
        4. Variables allows us to add trainable parameters to a graph.They are constructed with a type and initial value 
            -- When you call tf.Variable , variable are not initialized.To initialize all the variables in a TensorFlow program, you must explicity call a special operation as follows: 
        5. loss function measures how far apart the current model if from the provided data 
        6. The whole point of machine leanring is to find the correct model parameters automatically.
        7. tf.comtrib.learn is a high-level TensorFlow library that simplyfiles the mechanics of machine leanring
    
    **MNIST For ML Beginners**
        -- Just like programming has Hello World, machine leanring has MNIST 
        -- MNIST is a simple computer vision dataset.It consists of images of handwritten digits like these.it also includes labels for each image, telling us telling digit it is.
