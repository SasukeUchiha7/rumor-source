# Rumor Source Identification

### Getting Started
1. Make a virtual env to avoid any errors regarding compatibility etc.
    ```
    python -m venv my_venv
    source my_env/bin/activate
    ```
    This will create and activates the venv.

2. Clone this repo
    ```
    git clone https://github.com/SasukeUchiha7/rumor-source.git
    cd rumor-source
    ```

2. Install required packages

    This project uses some python modules which are listed in the requirements.txt file.
    To install these packages, run
    ```
    pip install -r requirements.txt
    ```
### Run
1. To run the project, run **run.py** file
    ```
    python run.py <algo_name> <dataset>
    ```
    **algo_name** : only 'ptva' or 'gmla' is available.
    
    **dataset** :should be the name of the edgelist file (csv) that should be present in the data folder.

    One example could be : **python run.py gmla dolphin**

2. All the plots will be stored in **plots** folder.