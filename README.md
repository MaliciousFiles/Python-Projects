# Project Title

Welcome to the Little Projects repository where you can find many small pieces of code including games and other fun programs. This is a python project repository and contains many different small projects that do not relate to each other and that are too small to be made into a repository (yet).

## Getting Started

To contribute to this repository you will have to fork the repository and then clone it to your local machine. You will then submit a pull request in order for your changes to go live. **You need git and python 3.6 or greater installed to proceed**

1. Fork the repository. [Learn how to fork a repo.](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
2. Clone the forked repository to your local machine. To do this, go to the home page of the repository and then click on the green `Clone or download` button. Copy the Https... . Then go to your command line, navigate to the directory where you want to clone it and use git to clone it by typing: `git clone ` + the copied url:
  ```
  $ git clone https://github.com/YOUR_USERNAME/Python-Projects.git
  ```
3. Finally, set up the original upstream repository. To do this, move into the Python-Projects directory. Then use git to set up the upstream repository as so:
  ```
  $ git remote add upstream https://github.com/MaliciousFiles/Python-Projects.git
  ```
4. You can then create a branch or make any other commits and changes. Once you have tested that your changes were successful, open a pull request and write a description of your changes.

### Prerequisites

* Python 3.6 or greater

### Installing

If you are a developer who wants to contribute, please follow the instructions below to set up the virtual environment needed for developing further.

First, make sure you have python 3.6 or greater installed as well as git.

Second, move to the directory in which you want to edit the file (using `cd`) and then clone the git repository:

```
$ git clone https://github.com/MaliciousFiles/Python-Projects.git
```

Third, let us set up the virtual environment. Start out by moving into the Python-Projects directory:

```
$ cd Python-Projects
```

Now let us set up the virtual environment. Here we will use virtualenv. You can install it by typing the following command: `sudo apt-get install python3-venv`. Now let us finish setting up the virtual environment. We will call it 'venv':

```
$ virtualenv venv
```

There is now a `venv` directory in `Python-Projects`. This is the folder for our virtual environment. Finally, let's install all of the needed dependencies in order to work on this repository:

```
$ source venv/bin/activate
$ cd venv
$ pip install -r requirements.txt
```
Now, you are ready to develop!

### An setup example


End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
