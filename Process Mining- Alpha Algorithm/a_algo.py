import pandas as pd
import pm4py
import os
os.environ['PATH']+=os.pathsep+'/usr/local/bin'
##1
# Preparing the log
event_log = pd.read_csv('running-exampleNew.csv', sep=';')
event_log = pm4py.format_dataframe(event_log, case_id='case_id', activity_key='activity', timestamp_key='timestamp')
start_activities = pm4py.get_start_activities(event_log)
end_activities = pm4py.get_end_activities(event_log)
print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

# Convert from CSV to XES
pm4py.write_xes(event_log, 'running-example-exported.xes')

# Algorithm alpha
log = pm4py.read_xes('running-example-exported.xes')
net, initial_marking, final_marking = pm4py.algo.discovery.alpha.algorithm.apply(log)
pm4py.view_petri_net(net, initial_marking, final_marking)

##2
# Preparing the log --- Resource
event_log = pd.read_csv('running-exampleNew.csv', sep=';')
event_log = pm4py.format_dataframe(event_log, case_id='case_id', activity_key='resource', timestamp_key='timestamp')
start_activities = pm4py.get_start_activities(event_log)
end_activities = pm4py.get_end_activities(event_log)
print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

# Convert from CSV to XES
pm4py.write_xes(event_log, 'running-example-exported.xes')

# Algorithm alpha
log = pm4py.read_xes('running-example-exported.xes')
net, initial_marking, final_marking = pm4py.algo.discovery.alpha.algorithm.apply(log)
pm4py.view_petri_net(net, initial_marking, final_marking)
