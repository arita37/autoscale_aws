
 Autoscale AWS allows to scale up virtual machines by invoking spot requests as per
 start and stop rules.

## Repo Index Docs
    Control + Find  to get reference files
    
https://github.com/arita37/autoscale_aws/blob/master/docs/doc_index.py





#  Autoscale AWS
 Autoscale AWS allows to scale up virtual machines (EC2s) by invoking spot requests as per start and stop rules.

## How it works!

   1. Every 5 minutes, the gihtub repo is pulled
   2. Scan the folders task
   3. Checking the tasks which havent started by comparing with S3 copies
   4. Start those tasks on Spot Instance
   5. Copy results to S3
   6. Close the Spot Instance

## Installation

### Installing process using pip

   1. Creation of virtual environments `python3 -m venv /path/to/new/virtual/environment`
   for details about creating Virtual Environment in Windows and Linux chick [this](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
   2. Change current directory to the new virtual environment `cd /path/to/new/virtual/environment`
   3. install autoscale_aws `pip install autoscale_aws`
   4. You can find AWS configuration in your local folder `C:\Users\${UserName}\.aws` once you install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html) 


### Installing process from github

   1. Getting current directory and assign its path to variable CURDIR by "CURDIR=`pwd`"
   2. Cloning the githup repo `git clone https://github.com/arita37/autoscale_aws/`
   3. Make new directory `mkdir ${CURDIR}/venvs`
   4. Make sure that virtualenv is installed, chick [this](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
   5. Create virtualenv `virtualenv -p python3 ${CURDIR}/venvs/autoscaleenv`
   6. Activate the virtualenv `source ${CURDIR}/venvs/autoscaleenv/bin/activate`
   7. Change directory to the autoscale_aws `cd ${CURDIR}/autoscale_aws`
   8. Installing pip `pip install -U pip`
   9. Installing the needed requirements `pip install -r requirements.txt`
   10. Export path `export PYTHONPATH=${CURDIR}/autoscale_aws/src:${PYTHONPATH}`
   11. Run `python src/autoscale_aws/batch_daemon_autoscale_cli.py --help`

## Getting Started

   1. Create S3 folder `mkdir s3_folder`
   2. Create tasks' folder in the S3 folder `mkdir s3_folder/tasks`
   3. Create tasks in the previous folder as below 
      ```
         mkdir s3_folder/tasks/mytask01/
         mkdir s3_folder/tasks/mytask02/
         mkdir s3_folder/tasks/mytask03/
      ```
   4. Every task should contain at least the below:
      ```
         main.sh   : bash script
         config.json  : json to config the task.
      ```
      *4.1* Example of config.json
      ```
         config.json : {
            'n_cpu' : 5,
            'ram'   : 4096
            'start_dt': Time to start :  '15:00'
         }
      ```
      *4.2* Daemon will generate  this file :
      ```
         mytask01_SUFFIX      SUFFIX=  _qstart     _qdone    _qignore     for started task, done task and ignore task.
      
         mytask01/status.json   :  { 'status' :  "nostarted/running/sucess/unknown",   'dt': "",
                           'start_dt': unixtime
                           'end_dt' : unixtime
         }
      ```
   5. Launch a micro-instance EC2 
   6. Install autoscale_aws as described [here](#installing-process-using-pip)
   7. Launch the daemon with the S3
         `batch_autoscale_daemon  --dir_task   /mys3folder/path/   --n_parallel_task  5    ## 5 tasks are running in parallel`
   8. Daemon will pick the tasks and check if it should start or not.


   Autoscale will pick up those ones, launch AWS instances, copy the folder to remote AWS, and launch main.sh on remote instances.
   Then stop them when the tasks are finished.

   The results are stored in S3 folders and it can be retrieved even the instances are closed on your local PC






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






