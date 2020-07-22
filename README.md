# Word Cloud

### Example

![workout query](/images/example_cloud.png)

This is not really a project, just a reminder for myself.
to install the dependencies just do:

## Setup locally

If you do not have Python installed, check the installation instructions for your platform here:

```http request
https://www.python.org/downloads/`
```

**Note that this project was built with Python 3.6 in mind.**

Once installed verify the installation on the terminal by typing:

```shell script
$ python --version # Python 3.6
```

**You will need to create a virtual environment.**

- This project uses `Pipenv` for the virtual environment.
    - If you do not already have Pipenv installed follow this guide to set it up for your platform:
    
    ```http request
    https://pypi.org/project/pipenv/
    ```
  
After successfully installing Pipenv you are required to change into the Pipenv virtual environment.

- In the project root input:

```shell script
$ pipenv shell
```

Time to install the dependencies into the virtual environment.

- In the project root on the terminal input:
 
```shell script
$ pipenv install -r requirements.txt
```

Note that the requirements file has additional libs in case you want to use stopwords (which I didnt).

Once the dependencies are installed then simple run:

```shell script
FILENAME=example_cloud.png python app.py
```

Where *FILENAME* represents the name of the file that will be saved (in the current directory by default).


 