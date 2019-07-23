Autoscale AWS using spot instances as per start and stop rules.

CURDIR=`pwd`
git clone <REPO URL>
mkdir ${CURDIR}/venvs
# Make sure virtualenv is installed
virtualenv -p python3 ${CURDIR}/venvs/autoscaleenv
source ${CURDIR}/venvs/autoscaleenv/bin/activate
cd ${CURDIR}/autoscaleaws
pip install -U pip
pip install -r requirements.txt
export PYTHONPATH=${CURDIR}/autoscaleaws/src:${PYTHONPATH}
python src/autoscale/batch_daemon_autoscale_cli.py --help
