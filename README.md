# devops-project
A small project to put devops principles and technologies into practice

# Usage

Build the container with ```docker build devops-project```

Run the container with ```docker run --name=devops-project --detached devops-project```

Check container logs with ```docker logs devops-project```

# Tools used

## Devops
- [Docker](https://docs.docker.com/) : Containerization

## Web
- [FastAPI](https://fastapi.tiangolo.com/) : Python web framework
- [openSenseMap](https://opensensemap.org/) : Open-source public api with sensor data around the world

## Development
- [Hadolint](https://github.com/hadolint/hadolint) : A dockerfile linter to ensure best practices are implemented
- [Pylint](https://pypi.org/project/pylint/) : A static code analyzer for python. Same goal as Hadolint but for python

# Git commit naming convention
- feat : for newly added functionnality
- fix : for bugfixing
- doc : for documentation updating (comments, readme, etc ...)
- refactor : for changes that do not have fucntionnal impact such as typos, unused variables/import or code "style" rewrite

# References

I learnt most of the skill and technologies required from the following resources :
- https://devopsroadmap.io/ : introduction to devops
- https://blog.stephane-robert.info/ : DevSecOps tutorials in french
- the documentations for the tools listed in [Tools](#tools-used)