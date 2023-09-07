# HTTP Server Project with Software Verification
This project targets software verification, Python programming, CI/CD tools, and networking. It employs an HTTP server developed in Python and a comprehensive test suite to verify the server's functionality and performance.

## Features
* Advanced verification infrastructure with multiple routes and HTTP methods.
* Comprehensive unit tests covering functionality and basic performance tests.
* Utilizes Git for version control. To get the full benefits, please clone this into your Git repository.
* Illustrates networking concepts by running a local HTTP server.
## Instructions
1. Run http_server.py to start the server.
2. In a separate terminal, run test_server.py to execute the comprehensive test suite.

The test suite utilizes Python's unittest framework for creating a variety of tests that validate both the functionality and performance of the server.

## CI/CD Integration
To integrate this project into a CI/CD pipeline, Jenkins or any other CI/CD tool can be configured to automatically run test_server.py whenever changes are pushed to the codebase. See .github/workflows/main.yml for GitHub Actions configuration for CI.

By creating a GitHub Actions workflow it allows to run my Python-based tests automatically whenever code is pushed or a pull request is made to the main branch. I attached example of the .github/workflows/main.yml file might look like for the Python-based HTTP server and its tests.

This .github/workflows/main.yml file defines a GitHub Actions workflow that triggers on push and pull_request events to the main branch. The job named build specifies that the tests will run on the latest Ubuntu environment. The steps include:

1. Checking out the repository code (actions/checkout@v2)
2. Setting up Python (actions/setup-python@v2)
3. Installing dependencies (pip install requests in this case)
4. Running the test (python -m unittest test_server.py)
Put this YAML code in a file located at .github/workflows/main.yml in your GitHub repository, and GitHub Actions will automatically pick up the workflow.

Note: Make sure to have a requirements.txt file or install any other necessary dependencies. In the example, I've installed requests as a standalone dependency because it's used in your test_server.py file.




