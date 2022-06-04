
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy

##Github For FastAPI Project - 
```
https://github.com/Ashishb21/FastAPI-Docker-Poetry
```
## AWS CDK Prerequisites
https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html

##Create a Fargate service 
https://docs.aws.amazon.com/cdk/v2/guide/ecs_example.html
##Install the AWS cli
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

## Configuring AWS 
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
## AWS Bootstrap
https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html
```commandline
cdk bootstrap aws://ACCOUNT-NUMBER-1/REGION-1 
```
## To destroy the stack 
```
cdk destroy 

```
