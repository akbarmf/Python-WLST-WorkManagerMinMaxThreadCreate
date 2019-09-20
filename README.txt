This Script is for create MaxThreadConstraints and MinThreadConstraints

Work Manager:
work,wmName,target:targetType|target2:targettype

Maximum Threads Constraint:
max,wmNameAssign,maxThreadName,target:targetType

Minimum Threads Constraint:
min,wmNameAssign,minThreadName,target:targetType







work		: tag that used to create work manager (don't change)
wmName		: your work manager name (change)
target		: targetName:Server  => for server target
		  targetName:Cluster => for cluster target
		  targetName:Server|targetName:Cluster => for target more than one


max		: tag that used to create Maximum Threads Constraint (don't change)
wmName		: Work Manager that want to assign this Max Threads Constraint (change)
maxThreadName	: Maximum Threads Constraint name you want to create (change)
target		: targetName:Server  => for server target
		  targetName:Cluster => for cluster target
		  targetName:Server|targetName:Cluster => for target more than one


min		: tag that used to create Minimum Threads Constraint (don't change)
wmName		: Work Manager that want to assign this Min Threads Constraint (change)
maxThreadName	: Minimum Threads Constraint name you want to create (change)
target		: targetName:Server  => for server target
		  targetName:Cluster => for cluster target
		  targetName:Server|targetName:Cluster => for target more than one