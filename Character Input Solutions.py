show databases then create databases<name> 
use <databases name>
to select a measureent from the list in databases
select * from cpu 
select * from <retention policy of databases>.<measureent>
	select * from monitor.httd

to check retention policies present on databases
show retention policies on <databases>

To create a retention policy
	create retention policy<rpname>on <databases> duration <hour min sec> replication 1 default
to alter retention policy 
	alter retention policy <default.>on <databases>
	alter retention policy one_hour on newDB default

to cheak continuous queries
	show continuous queries
	
run node js program
select * from <databases>.<retention policy name>.<measureent name>
	select * from newDB.one_hour.mem

continuous queries

	create continuous query <query name> on <databases name> resample every 1m
	begin
	select <operation if any > into <databases.name><rpname><new measureent name> from <databases.name><rpname>
	<old measureent name> group by time 30s
	end

create continuous queries cq1 on newDB  resample every 1m begin select mean (abc) as mean_abc, into newDB.one_hour.measur
from newDB.two_hr.mes group by time 30s end



create databases newDB
show databases
use newDB
show retention policies
create retention policies five_hour on newDB duration 1h repliocation 1

create continuous query test on newDB resample every 1m
begin
select mean(mem) as mean_mean, max(cpu) as max_cpu, stddev(abc) as std_abc into newDB.fivehour from mem group by time 30s
end


kapacitor list tasks
kapacitor define newTick -tick newTick.tick
kapacitor define newTick.tick -type strem -dbrp newDB.one_hour
kapacitor define<name>.tick <file path> -type <type> -drop <db><rp>
kapacitor show newTick
kapacitor enable newtask
