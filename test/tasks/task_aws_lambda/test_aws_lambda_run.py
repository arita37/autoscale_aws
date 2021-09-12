import pytest
from moto import mock_lambda
from src.autoscale_aws.util_aws import aws_lambda_run

@pytest.fixture
def mock_AWS(mocker):
    aws_mocker = mocker.patch('src.autoscale_aws.util_aws.AWS').return_value
    aws_mocker.v = {'AWS_REGION': 'test_region'}
    aws_mocker.aws_accesskey_get.return_value = ('test_access', 'test_secret')
    return aws_mocker   

@pytest.fixture
def mock_boto(mocker):
    boto_mocker = mocker.patch('src.autoscale_aws.util_aws.boto3.client').return_value
    boto_mocker.create_function.return_value = True
    boto_mocker.invoke.return_value = True
    boto_mocker.delete_function.return_value = True

    return boto_mocker

@mock_lambda
def test_aws_lambda_run(mock_AWS, mock_boto):
    aws_lambda_run()
    mock_boto.create_function.assert_called()
    mock_boto.invoke.assert_called()
    mock_boto.delete_function.assert_called()