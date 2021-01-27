# moonboard_machine_learning

 Software architecture: 
 
 Database:
 - moon-problems.db

Jupyter notebook pre-processing scripts:
- pre-process_database.ipynb: This notebook extracts the problems from the database and transforms them into the 12 submatrices of size 13x13 that are the individual inputs to the neural network (as described in the Presentation called "Machine Learning Moonboard Problems with Custom Convolutional Network"). Then the dataset is separated into 70% train and 30% test sets that are representative of the general set. These train/test sets are saved as “problems_train.npy”, “problems_test.npy”. “grades_train.npy”, “grades_test.npy”. Then, some data exploration is done and plotted.
- get_hold_difficulty.ipynb: This notebook classifies the holds as easy (0.33), medium (0.66) and hard (1), based on how frequently they appear in each kind of climb. It saves the difficulties as csv file called “hold_difficulty.csv”
- draw_problem.py: This is a helper script that draws the problem submatrices or the full problems starting from the holds in text format (ie [A5, F13, H8, etc]). It opens the “hold_difficulty.csv” to know what values to use at the center of the submatrices.

Machine learning Jupyter notebooks and Python scripts:
- Machine_learning_custom_convolution.ipynb: Runs machine learning and evaluates the accuracy of the model. Preliminary machine learning runs were done to determine the adequate number of epochs etc. Only best result is shown here. 


Jupyter notebook webscraping -- Proof of principle:
- WebScrape_Moonboard.ipynb: Shows a basic sequence of steps to download new Moonboard problems added to the website since the database of problems we have was last updated. It requires the coder to input password and username manually and possibly supervise the Selenium browser, though, since they have anti-robot software.
