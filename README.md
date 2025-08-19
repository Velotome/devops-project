# devops-project
A small project to put devops principles and technologies into practice

# Usage

Build the container with ```docker build --tag devops-project .```

Run the container with ```docker run --name=devops-project -d --network host -p 8000:8000 devops-project```

Check container logs with ```docker logs -f devops-project```

Alternatively, you can use the test-docker.sh that will remove the old container before creating a new one and running it. This is what I used while developping the app

# Tools used

## Devops
- [Docker](https://docs.docker.com/) : Containerization

## Web
- [FastAPI](https://fastapi.tiangolo.com/) : Python web framework
- [openSenseMap](https://opensensemap.org/) : Open-source public api with sensor data around the world

## Development
- [Visual Studio Code](https://code.visualstudio.com/) : IDE (not really and IDE but kinda)
- [Hadolint](https://github.com/hadolint/hadolint) : A dockerfile linter to ensure best practices are implemented
- [Pylint](https://pypi.org/project/pylint/) : A static code analyzer for python. Same goal as Hadolint but for python

## Testing
- [Pytest](https://docs.pytest.org/en/stable/) : Python testing framework, used for unit test

## Git commit naming convention
- feat : for newly added functionnality
- fix : for bugfixing
- doc : for documentation updating (comments, readme, etc ...)
- refactor : for changes that do not have fucntionnal impact such as typos, unused variables/import or code "style" rewrite
- prod : for changes concerning docker, jenkins, scripts and other production related modification

# References

I learnt most of the skill and technologies required from the following resources :
- https://devopsroadmap.io/ : introduction to devops
- https://blog.stephane-robert.info/ : DevSecOps tutorials in french
- the documentations for the tools listed in [Tools](#tools-used)