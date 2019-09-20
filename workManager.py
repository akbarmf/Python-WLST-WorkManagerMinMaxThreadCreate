from java.io import FileInputStream

def target(serverTarget):
    targetsForDeployment = []
    targets = serverTarget.split('|')
    for target in targets: 
      if(target == '') :
        break;
      index=target.find(':')
      serverName=target[0:index]
      type=target[index+1:]
      nextName =str('com.bea:Name='+serverName+',Type='+type)
      targetsForDeployment.append(ObjectName(nextName))
    set('Targets',jarray.array(targetsForDeployment, ObjectName))
    #return targetsForDeployment

def createWorkManager(line):
  try:
    startEdit()
    cd('/')
    domainName = cmo.getName()
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,wmName,serverTarget) = items
     
    # Check if Work Manager already exist	 
    cd('/SelfTuning/' + domainName)
    redirect('/dev/null','false')
    exist = ls('WorkManagers/',returnMap='true')
    if wmName in exist:
      print('\n!!!! Work Manager: ' + wmName + ' already exist !!!!\n')
      exit(exitcode=1,defaultAnswer='y')
	
    # Create Work Manager
    print('\nCreate Work Manager: ' + wmName )
    cmo.createWorkManager(wmName)
    
    # Target to server/cluster
    cd('/SelfTuning/' + domainName + '/WorkManagers/' + str(wmName))
    target(serverTarget)
    #set('Targets',jarray.array(targetsForDeployment, ObjectName))
	
    save()
    activate()
	
  except Exception, e:
    print e
	


def createMaxWM(line):
  try:
    startEdit()
    cd('/')
    domainName = cmo.getName()
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,wmName,maxName,count,serverTarget) = items
     
    # Check if Maximum Threads Constraint name exist 
    cd('/SelfTuning/' + domainName)
    redirect('/dev/null','false')
    exist = ls('MaxThreadsConstraints/',returnMap='true')
    if maxName in exist:
      print('\n!!!! Maximum Threads Constraint: ' + maxName + ' already exist !!!!\n')
      exit(exitcode=1,defaultAnswer='y')
    print('\nCreate MaxThreadConstrain: ' + maxName )
	
    # Create MaxThreadsConstraints 
    cmo.createMaxThreadsConstraint(maxName)
    
    # Target to server/cluster
    cd('/SelfTuning/' + domainName + '/MaxThreadsConstraints/' + str(maxName))
    target(serverTarget)
    #set('Targets',jarray.array(targetsForDeployment, ObjectName))
	
    # Set Up Count size
    cmo.setCount(int(count))
	
    # Assign to Work Manager
    if wmName != "None":
      redirect('/dev/null','false')
      check=ls('/SelfTuning/' + domainName + '/WorkManagers/',returnMap='true')
      if wmName not in check:
        print('Assign Failed, Work Manager ' + wmName + ' not found !!!!')
      else:
        print('Assign Max Threads Constraint: '+maxName+ ' to Work Manager: ' +wmName)
        cd('/SelfTuning/' + domainName + '/WorkManagers/' + str(wmName))
	cmo.setMaxThreadsConstraint(getMBean('/SelfTuning/' + domainName + '/MaxThreadsConstraints/' + str(maxName)))
    else:
      print('Not Assign this Threads Constraint to Work Manager')

    save()
    activate()
	
  except Exception, e:
    print e
	
def createMinWM(line):
  try:
    startEdit()
    cd('/')
    domainName = cmo.getName()
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,wmName,minName,count,serverTarget) = items
    
    # Check if Minimum Threads Constraint exist	
    cd('/SelfTuning/' + domainName)
    redirect('/dev/null','false')
    exist = ls('MinThreadsConstraints/',returnMap='true')
    if minName in exist:
      print('\n!!!! Minimum Threads Constraint: ' + minName + ' already exist !!!!\n')
      exit(exitcode=1,defaultAnswer='y')
    print('\nCreate MinThreadConstrain: ' + minName )
	
    # Create Minimum Threads Constraint
    cmo.createMinThreadsConstraint(minName)
	
    # Target to Server/Cluster
    cd('/SelfTuning/' + domainName + '/MinThreadsConstraints/' + str(minName))
    target(serverTarget)
    #set('Targets',jarray.array(targetsForDeployment, ObjectName))
	
    # Set up count Size
    cmo.setCount(int(count))
	
    # Assign to Work Manager
    if wmName != "None":
      redirect('/dev/null','false')
      check=ls('/SelfTuning/' + domainName + '/WorkManagers/',returnMap='true')
      if wmName not in check:
        print('Assign Failed, Work Manager ' + wmName + ' not found !!!!')
      else:
        print('Assign Min Threads Constraint: '+minName+ ' to Work Manager: ' +wmName)
        cd('/SelfTuning/' + domainName + '/WorkManagers/' + str(wmName))
   	cmo.setMinThreadsConstraint(getMBean('/SelfTuning/' + domainName + '/MinThreadsConstraints/' + str(minName)))
    else:
      print('Not Assign this Threads Constraint to Work Manager')
	
    save()
    activate()
	
  except Exception, e:
    print e
	
def main():
  propInputStream = FileInputStream(sys.argv[1])
  configProps = Properties()
  configProps.load(propInputStream)
   
  url=configProps.get("adminUrl")
  username=configProps.get("importUser")
  password=configProps.get("importPassword")
  csvLoc=configProps.get("csvLoc")
  
  connect(username , password , url)
  edit()
  file=open(csvLoc)
  for line in file.readlines():
    if line.strip().startswith('work'):
      createWorkManager(line)
    elif line.strip().startswith('max'):
      createMaxWM(line)
    elif line.strip().startswith('min'):
      createMinWM(line)
    else:
      continue
	
  disconnect()

main()
	
