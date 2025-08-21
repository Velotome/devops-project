# devops-project
A small project to put devops principles and technologies into practice

# Usage

Build the app container with ```docker build --tag app --target app .```

Run the app container with ```docker run --name=app -d --network host app```

Check container logs with ```docker logs -f app```

# Testing

With an app container running as shown in [previous step](#usage)

Build the testing container with ```docker build --tag test --target test .```

Run the container with ```docker run --name=test -d --network host test```

Check container logs with ```docker logs -f test```

# Tools used

## Devops
- [Docker](https://docs.docker.com/) : Containerization

## CI/CD
- [Github Actions](https://github.com/features/actions) : CI/CD workflow similar to jenkins

## Web
- [FastAPI](https://fastapi.tiangolo.com/) : Python web framework
- [openSenseMap](https://opensensemap.org/) : Open-source public api with sensor data around the world

## Development
- [Git & Github](https://github.com/) : version control system and hosting
- [Visual Studio Code](https://code.visualstudio.com/) : IDE (not really and IDE but kinda)
- [Hadolint](https://github.com/hadolint/hadolint) : A dockerfile linter to ensure best practices are implemented
- [Pylint](https://pypi.org/project/pylint/) : A static code analyzer for python. Same goal as Hadolint but for python
- [Black](https://github.com/psf/black) : Code formatter

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
