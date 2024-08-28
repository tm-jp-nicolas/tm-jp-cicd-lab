# CI/CD - Github Actions Lab

### (Thinking Machines Talent Engine Lab 6 - Intro to CI/CD)

This is a small project that packs a lot of insights. With only a few yaml files, it manages to impart knowledge regarding Github Actions:
  - Creating Environments, Environment Varibles, and Secrets
  - Utilization of Template for workflow reusability
  - Running a Python script through a job
  - Printing a secret variable
  - Utilizing the Environment to switch to different environment variables

Implementation:
  - I started from the smallest unit until the last
  - I created a flat workflow with one job that has two steps (run python and print secret) to ensure that all the logic works
  - After making sure that everything works, I broke the two down into separate jobs
  - I then started to incorporate the templating
  - Once successful, I created another workflow for the other environment

    
