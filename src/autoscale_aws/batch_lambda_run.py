from util_aws import aws_lambda_run

import shutil

def batch_lambda_run():
    shutil.make_archive('src/autoscale_aws/aws/lambda', 'zip', 'src/autoscale_aws/aws/lambda')
    aws_lambda_run()
    # TODO: Remove zip file

batch_lambda_run()