# AWS S3 File Management using Flask

## Getting Started

### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [Pipenv](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)
- [ ] [AWS CLI Tool](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
- [ ] [Git]()
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/luisseneto/aws-s3-file-management
```

2. Check into the cloned repository
```
$ cd aws-s3-file-management
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$ pipenv install && pipenv shell
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

4. Configure AWS CLI
```
$ aws configure
```

5. Create a bucket on AWS Dashboard and update it on the `app.py` file on line 10.

6. Run the application
```
$ python app.py
```

7. Navigate to http://localhost:5000/storage
