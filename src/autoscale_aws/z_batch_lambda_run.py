import os
import shutil

from util_aws import aws_lambda_run


def batch_lambda_run():
    folder = 'src/autoscale_aws/aws'
    lambda_folder = f'{folder}/lambda'
    shutil.make_archive(lambda_folder, 'zip', lambda_folder)
    aws_lambda_run()
    os.remove(f'{folder}/lambda.zip')



