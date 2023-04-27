[![build](https://github.com/JGCRI/pytemplate/actions/workflows/build.yml/badge.svg)](https://github.com/JGCRI/pytemplate/actions/workflows/build.yml)
[![docs](https://github.com/JGCRI/pytemplate/actions/workflows/docs.yml/badge.svg)](https://github.com/JGCRI/pytemplate/actions/workflows/docs.yml)
[![tests](https://github.com/JGCRI/pytemplate/actions/workflows/test.yml/badge.svg)](https://github.com/JGCRI/pytemplate/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/JGCRI/pytemplate/branch/main/graph/badge.svg?token=2EWDAQI07B)](https://codecov.io/gh/JGCRI/pytemplate)

# Introduction

`pytemplate` is a template for creating a basic Python package with Continuous Integration (CI) via GitHub actions in the following steps:

1. Clone or Copy
2. Update Package Information
3. Update Package Modules
4. Update Package Documentation
5. Github Actions for Continuous Integration

The folder structure is as shown below:

![pytemplate_package_structure](extras/pytemplate_package_structure.png)


# 1 Clone or Copy

Navigate directly to https://github.com/JGCRI/pytemplate, click the shiny green button that says `Use this template` and be on your way.

You can also clone the template to view the files locally and then copy into your own repo as needed:

```bash
git clone https://github.com/JGCRI/pytemplate.git
```

# 2 Update Package Information

Update your information (package name and other details) in the following files:

- README.md
- setup.py
- LICENSE
- pytemplate (Rename this folder to your new package name)

# 3 Update Package Modules

This is where you write the main code for your model. We have include some key modules and tests. You should write tests for all your modules as you develop them.

- pytemplate\model.py (This is your main model class. Update all module names as modules are updated)
- pytemplate\tests\test_package.py (Update tests for all modules as you update them)
- pytemplate\get_data.py (Update the path to your test data)
- pytemplate\read_config.py (Used to read a configuration file with model settings)
- pytemplate\read_data.py (Used to read data files for your model)
- pytemplate\method.py (This is where you do your main model operations. You can write multiple methods within this file or if you have many methods you can group them into separate files e.g. spatial_downscaling.py, temporal_downscaling.py)
- pytemplate\logger.py (This method starts the logger and is called in model.py. After this is loaded you can log all comments, errors and excution times throughout your code by using the logging module.)
- pytemplate\diagnsotics.py (Update this to write your diagnostic scripts that test how various modules are performing.)
- pytemplate\clean_up.py (Update this script to delete unecessary files, clean up memory and close out the model.)

# 3 Update Package Documentation

Update each of the following files to generate clean, clear documentation. When you push your changes to github the github actions described in the next section will automatically build the documentation page online for you. An example for this repo is available at: https://jgcri.github.io/pytemplate/. 

- docs\source\conf.py
- docs\source\contributing.rst
- docs\source\getting_started.rst
- docs\source\index.rst
- docs\source\license.rst
- docs\source\modules.rst
- docs\source\tests.rst
- docs\source\user_guide.rst

Once your docs github action is complete (see below) you need to follow the following steps to get your documentation page live online:

![pytemplate_package_structure](extras/pytemplate_activate_docs.png)


# 4 Github Actions

Update the github actions for continuous integration build checks, docs, testing and an example paper.

- .github\workflows\build.yml
