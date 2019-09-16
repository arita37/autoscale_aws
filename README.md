
 Autoscale AWS allows to scale up virtual machines by invoking spot requests as per
 start and stop rules.



 ```
 To publish
cd repo
python pypi.py  pblish


 ```


```
Create a folder of tasks.
   /tasks/mytask01/
   /tasks/mytask02/
   /tasks/mytask03/


Autoscale will pick up those ones, launch AWS instances,
copy the folder to remote AWS, and launch main.sh on remote instances.
and stop them when the tasks are finished.


The results are stored in S3 folders and it can be retrieved
even the instances are closed on your local PC


```



```

Install process  from pip :

cd yourenv
pip install autoscale_aws

Configuration is in 
YOURHOME/.aws/


```




```

Install process  from github :

CURDIR=`pwd`
git clone https://github.com/arita37/autoscale_aws/
mkdir ${CURDIR}/venvs
Make sure virtualenv is installed
virtualenv -p python3 ${CURDIR}/venvs/autoscaleenv
source ${CURDIR}/venvs/autoscaleenv/bin/activate
cd ${CURDIR}/autoscale_aws

pip install -U pip
pip install -r requirements.txt
export PYTHONPATH=${CURDIR}/autoscale_aws/src:${PYTHONPATH}
python src/autoscale_aws/batch_daemon_autoscale_cli.py --help

```






