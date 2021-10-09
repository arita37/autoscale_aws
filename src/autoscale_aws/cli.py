# -*- coding: utf-8 -*-
HELP ="""
########  Usage 
    pip install --upgrade awscli

## method 1
aws_run  batch_lambda  --path  src/autoscale_aws/aws   


## method 2
python cli.py   batch_lambda  --path  src/autoscale_aws/aws 


"""
import argparse, os
import shutil
###################################################


def os_remove(filepath):
    try:
        os.remove(filepath)
    except : pass


def batch_lambda_run(folder = 'src/autoscale_aws/aws'):
    from util_aws import aws_lambda_run
    lambda_folder = f'{folder}/lambda'
    shutil.make_archive(lambda_folder, 'zip', lambda_folder)
    aws_lambda_run()
    os.remove(f'{folder}/lambda.zip')


######################################################################################################
def run_cli():
    """ Usage


    """
    p   = argparse.ArgumentParser()
    add = p.add_argument

    add('task', metavar='task', type=str, nargs=1, help='')

    #### Extra
    add("--path",    type=str, default=None,     help = "path")

    args = p.parse_args()



    if args.task[0] == 'help':
        print(HELP)

    ###############################################################################################        


    if args.task[0] == 'batch_lambda':
        batch_lambda_run( args.path, )



#############################################################################
if __name__ == "__main__":
    run_cli()

