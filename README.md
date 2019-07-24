Autoscale AWS using spot instances as per start and stop rules.

CURDIR=`pwd`
git clone https://github.com/arita37/autoscale_aws/
mkdir ${CURDIR}/venvs
# Make sure virtualenv is installed
virtualenv -p python3 ${CURDIR}/venvs/autoscaleenv
source ${CURDIR}/venvs/autoscaleenv/bin/activate
cd ${CURDIR}/autoscale_aws
pip install -U pip
pip install -r requirements.txt
export PYTHONPATH=${CURDIR}/autoscale_aws/src:${PYTHONPATH}
python src/autoscale_aws/batch_daemon_autoscale_cli.py --help
