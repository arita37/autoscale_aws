

src/autoscale_aws/__init__.py


src/autoscale_aws/aws/lambda/main.py
-------------------------functions----------------------
lambda_handler(event, context)



src/autoscale_aws/batch_daemon_autoscale_cli.py
-------------------------functions----------------------
autoscale_main()
ec2_config_build_template(amiId, instance_type = 't3.small', spot_cfg_file = '/tmp/ec_spot_config', keypair = None)
ec2_get_spot_price(instance_type = 't3.small')
ec2_instance_backup(instances_list, folder_list = ["zlog/"], folder_backup = "/home/ubuntu/zs3drive/backup/")
ec2_instance_getallstate(instance_type = 't3.small', key_file = None)
ec2_instance_initialize_ssh(args, key_file)
ec2_instance_stop(instance_list)
ec2_instance_usage(instance_id = None, ipadress = None, key_file = None)
ec2_keypair_get(keypair)
ec2_spot_instance_list()
ec2_spot_price_value(region, instance_type = 't3.small')
ec2_spot_start(amiId, instance_type, spot_price, region = 'us-west-2', spot_cfg_file = '/home/ubuntu/test/ec_spot_config', keypair = None, waitsec = 100)
instance_get_ncpu(instances_dict)
instance_start_rule(task_folder, global_task_file)
instance_stop_rule(task_folder, global_task_file, instance, key_file)
load_arguments()
log(*argv)
os_folder_copy(from_folder_root, to_folder, isoverwrite = False, exclude_flag = "ignore")
ps_check_process(name)
task_get_from_github(repourl, reponame = "tasks", branch = "dev", to_task_folder = "/home/ubuntu/zs3drive/tasks/", tmp_folder = "/home/ubuntu/data/ztmp/")
task_get_list_valid_folder(folder, script_regex = r"main\.(sh|py)
task_get_list_valid_folder_new(folder_main, global_task_file)
task_getcount(folder_main, global_task_file)
task_getcount_cpurequired(folder_main, global_task_file)
task_globalfile_reset(global_task_file = None)
task_isvalid_folder(folder_main, folder, folder_check)
task_put_to_github(repourl, branch = "dev", from_taskout_folder = "/home/ubuntu/zs3drive/tasks_out/", repo_folder = "/home/ubuntu/data/github_tasks_out/")



src/autoscale_aws/batch_daemon_launch_cli.py
-------------------------functions----------------------
get_list_valid_task_folder(folder, script_name = "main")
global_task_file_save(folder, folder_check, global_task_file)
isvalid_folder(folder_main, folder, folder_check, global_task_file)
load_arguments()
log(*argv)
main()
main2()
main3()
os_wait_policy(waitsleep = 15, cpu_max = 95, mem_max = 90.0)
subprocess_launch(foldername, main_file)



src/autoscale_aws/batch_daemon_monitor_cli.py
-------------------------functions----------------------
load_arguments()
log(*argv)
logcpu(*argv)



src/autoscale_aws/cli.py
-------------------------functions----------------------
batch_lambda_run(folder  =  'src/autoscale_aws/aws')
os_remove(filepath)
run_cli()



src/autoscale_aws/task_template/main_run.py


src/autoscale_aws/task_template/task_config.py
-------------------------functions----------------------
load_arguments()
os_copy_local_to_s3(taskout_local, taskout_s3_root)
os_rename_taskfolder(task_name, taskout_s3_root, suffix = "_qdone")



src/autoscale_aws/util_aws.py
-------------------------functions----------------------
aws_conn_getallregions(conn = None)
aws_conn_getinfo(conn)
aws_ec2_allocate_eip(instance_id, conn = None, eip_allocation_id = None, eip_public_ip = None, allow_reassociation = False)
aws_ec2_allocate_elastic_ip(conn, instance_id = '', elastic_ip = '', region = '')
aws_ec2_ami_create(conn, ip_address = '', ami_name = '')
aws_ec2_get_folder(ipadress, fromfolder1, tofolder1)
aws_ec2_get_instanceid(conn, filters = None)
aws_ec2_get_instances(con = None, attributes = None, filters = None, csv_filename = ".csv")
aws_ec2_getfolder(remotepath, sftp)
aws_ec2_getfrom_ec2(fromfolder, tofolder, host)
aws_ec2_printinfo(instance = None, ipadress = "", instance_id = "")
aws_ec2_put(fromfolder='D = 'D:/_d20161220/', tofolder = '/linux/batch', host = '')
aws_ec2_putfile(fromfolder='d = 'd:/file1.zip', tofolder = '/home/notebook/aapackage/', host = '')
aws_ec2_putfolder(fromfolder='D = 'D:/_d20161220/', tofolder = '/linux/batch', host = '')
aws_ec2_res_start(conn, region, key_name, ami_id, inst_type = "cx2.2", min_count  = 1, max_count = 1, pars = None)
aws_ec2_res_stop(conn, ipadress = "", instance_id = "")
aws_ec2_spot_start(conn, region, key_name = "ecsInstanceRole", inst_type = "cx2.2", ami_id = "", pricemax = 0.15, elastic_ip = '', pars = None)
aws_ec2_spot_stop(conn, ipadress = "", instance_id = "")
aws_ec2_ssh_cmd(cmdlist = ["ls "], host = 'ip', doreturn = 0, ssh = None, username = 'ubuntu', keyfile = '')
aws_ec2_ssh_create_con(contype = 'sftp/ssh', host = 'ip', port = 22, username = 'ubuntu', keyfilepath = '', password = '', keyfiletype = 'RSA', isprint = 1)
aws_ec2_ssh_python_script(python_path = '/home/ubuntu/anaconda2/bin/ipython', script_path = "", args1 = "", host = "")
aws_lambda_run(function_name  =  f'lambda_from_util_aws', runtime             =  'python3.7', dir_codesource_zip  =  'src/autoscale_aws/aws/lambda.zip', lambda_folder       =  'src/autoscale_aws/aws/lambda', role               = 'arn =  'arn:aws:iam::495134704719:role/lambda_from_util_aws', handler             =  'main.lambda_handler', layer              = 'arn =  'arn:aws:lambda:us-east-2:495134704719:layer:libraries:1', **kw)
aws_s3_file_read(bucket1, filepath)
aws_s3_folder_printtall(bucket_name = 'zdisk')
aws_s3_get(s3dir)
aws_s3_getbucketconn(s3dir)
aws_s3_put(fromdir_file = 'dir/file.zip', todir = 'bucket/folder1/folder2')
aws_s3_url_split(url)
cli_windows_start_spot()
ec2_config_build_template_cli(instance_type, amiId = None, keypair = None, default_instance_type = None, spot_cfg_file = None)
ec2_get_spot_price(instance_type)
ec2_instance_getallstate_cli(default_instance_type = "t3.medium")
ec2_instance_stop(instance_list)
ec2_instance_usage(instance_id = None, ipadress = None)
ec2_spot_instance_list()
ec2_spot_start_cli(instance_type, spot_price, region = None, waitsec = 100)
exists_dir(dirname)
exists_file(fname)
get_host_public_ipaddress()
json_from_file(jsonfile, defval = None)
os_file_getname(path)
os_file_getpath(path)
os_folder_copy(src, dst, symlinks = False, pattern1 = "*.py", fun_file_toignore = None)
os_folder_delete(tempfolder)
os_split_dir_file(dirfile)
os_system(cmds, stdout_only = 1)
os_zip_checkintegrity(filezip1)
os_zipfolder(dir_tozip = "", zipname = "", dir_prefix = True, iscompress = True)
sftp_isdir(path, sftp)
sleep2(wsec)
ssh_cmdrun(hostname, key_file, cmdstr, remove_newline = True, isblocking = True)
ssh_put(hostname, key_file, remote_file, msg = None, filename = None)
test_all()
tofloat(value, default = 0.0)
z_key_splitinto_dir_name(keyname)

-------------------------methods----------------------
AWS.__init__(self, name = None, keypair = None, keypem = None)
AWS.aws_accesskey_get(self)
AWS.aws_conn_create(self, region = '', access = '', key = '')
AWS.aws_conn_create_windows(self, aws_region = '')
AWS.ec2_keypair_get(self, keypair = "")
AWS.get_ec2_conn(self)
AWS.get_keypair(self)
AWS.set_attribute(cls, key, value)
AWS.set_keypair(self, keypairname, keypairlocation)
aws_ec2_ssh.__init__(self, hostname, username = 'ubuntu', key_file = None, password = None)
aws_ec2_ssh._help_ssh(self)
aws_ec2_ssh.cmd(self, cmdss)
aws_ec2_ssh.cmd2(self, cmd1)
aws_ec2_ssh.command(self, cmd)
aws_ec2_ssh.command_list(self, cmdlist)
aws_ec2_ssh.get(self, remotefile, localfile)
aws_ec2_ssh.get_all(self, remotepath, localpath)
aws_ec2_ssh.jupyter_kill(self)
aws_ec2_ssh.jupyter_start(self)
aws_ec2_ssh.listdir(self, remotedir)
aws_ec2_ssh.put(self, localfile, remotefile)
aws_ec2_ssh.put_all(self, localpath, remotepath)
aws_ec2_ssh.put_all_zip(self, suffixfolder = "", fromfolder = "", tofolder = "", use_relativepath = True, usezip = True, filefilter = "*.*", directorylevel = 1, verbose = 0)
aws_ec2_ssh.python_script(self, ipython_path = '/home/ubuntu/anaconda3/bin/ipython ', script_path = "", args1 = "")
aws_ec2_ssh.sftp_walk(self, remotepath)
aws_ec2_ssh.write_command(self, text, remotefile)
dict2.__init__(self, adict)


src/autoscale_aws/util_batch.py
-------------------------functions----------------------
batch_generate_hyperparameters(hyperparam_dict, outfile_hyperparam)
batch_parallel_subprocess(hyperparam_file, subprocess_script, os_python_path = None, waitime = 5)
batch_run_infolder(task_folders, suffix = "_qstart", main_file_run = "main.py", waitime = 7, os_python_path = None, log_file = None, )
log(*argv)
os_cmd_generate(task_folder, os_python_path = None)
os_folder_create(folder)
os_folder_rename(old_folder, new_folder)
os_python_path()
os_wait_policy(waitsleep = 15, cpu_max = 95, mem_max = 90.0)



src/autoscale_aws/util_cpu.py
-------------------------functions----------------------
log(*argv)
monitor_maintain()
monitor_nodes()
np_avg(list)
np_pretty_nb(num, suffix = "")
os_environment()
os_extract_commands(csv_file, has_header = False)
os_generate_cmdline()
os_getparent(dir0)
os_is_wndows()
os_launch(commands)
os_python_environment()
ps_all_children(pr)
ps_find_procs_by_name(name = r"((.*/)
ps_get_computer_resources_usage()
ps_get_cpu_percent(process)
ps_get_memory_percent(process)
ps_get_process_status(pr)
ps_is_issue(p)
ps_is_issue_system()
ps_net_send(tperiod = 5)
ps_process_isdead(pid)
ps_process_monitor_child(pid, logfile = None, duration = None, interval = None)
ps_terminate(processes)
ps_wait_process_completion(subprocess_list, waitsec = 10)
ps_wait_ressourcefree(cpu_max = 90, mem_max = 90, waitsec = 15)

-------------------------methods----------------------
IOThroughputAggregator.__init__(self)
IOThroughputAggregator.aggregate(self, cur_read, cur_write)
NodeStats.__init__(self, num_connected_users = 0, num_pids = 0, cpu_count = 0, cpu_percent = None, mem_total = 0, mem_avail = 0, swap_total = 0, swap_avail = 0, disk_io = None, disk_usage = None, net = None, )
NodeStats.mem_used(self)
NodeStatsCollector.__init__(self, pool_id, node_id, refresh_interval = _DEFAULT_STATS_UPDATE_INTERVAL, app_insights_key = None, )
NodeStatsCollector._collect_stats(self)
NodeStatsCollector._get_disk_io(self)
NodeStatsCollector._get_disk_usage(self)
NodeStatsCollector._get_network_usage(self)
NodeStatsCollector._log_stats(self, stats)
NodeStatsCollector._sample_stats(self)
NodeStatsCollector._send_stats(self, stats)
NodeStatsCollector.init(self)
NodeStatsCollector.run(self)


src/autoscale_aws/util_log.py
-------------------------functions----------------------
create_appid(filename)
create_logfilename(filename)
create_uniqueid()
load_arguments(config_file = None, arg_list = None)
logger_handler_console(formatter = None)
logger_handler_file(isrotate = False, rotate_time = "midnight", formatter = None, log_file_used = None)
logger_setup(logger_name = None, log_file = None, formatter = FORMATTER_1, isrotate = False, isconsole_output = True, logging_level = logging.DEBUG, )
logger_setup2(name = __name__, level = None)
printlog(s = "", s1 = "", s2 = "", s3 = "", s4 = "", s5 = "", s6 = "", s7 = "", s8 = "", s9 = "", s10 = "", app_id = "", logfile = None, iswritelog = True, )
writelog(m = "", f = None)



src/autoscale_aws/z_batch_lambda_run.py
-------------------------functions----------------------
batch_lambda_run()

