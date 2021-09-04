
 Autoscale AWS allows to scale up virtual machines by invoking spot requests as per
 start and stop rules.




## Usage
```
1) Create a folder of tasks in a S3 folder
   /tasks/mytask01/
   /tasks/mytask02/
   /tasks/mytask03/

A minimal task is defined by :
   main.sh   : bash script
   config.json  : json to config the task.
   
   config.json : {
      'n_cpu' : 5,
      'ram'   : 4096
      'start_dt': Time to start :  '15:00'
   }
   

  Daemon will generate  this file :
     mytask01_SUFFIX      SUFFIX=  _qstart     _qdone    _qignore     for started task, done task and ignore task.
  
  
     mytask01/status.json   :  { 'status' :  "nostarted/running/sucess/unknown",   'dt': "",
                      'start_dt': unixtime
                      'end_dt' : unixtime
     }


2) Launch a micro-instance EC2 


3) pip install autoscale_aws


4) Launch the daemon with the S3
  batch_autoscale_daemon  --dir_task   /mys3folder/path/   --n_parallel_task  5    ## 5 tasks are running in parallel
  
  
5) daemon will pick the tasks
    and check if it should start or not.






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






