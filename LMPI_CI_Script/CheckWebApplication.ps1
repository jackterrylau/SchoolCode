Import-Module WebAdministration

# Get Argument from command line input
#$app = $args[0]
$app = "LMPI"
$pool = "$($app)_pool"

# Out-String : make the output of pipe as a string object.
$r = $false
$webapps = Get-WebApplication | select-Object path | ForEach {"$($_.path)"}
foreach ($ee in $webapps) {
  if ($ee -eq "/$($app)") {$r = $true}
}

if($r -eq $true) {
  echo "The $app web application has been created."
}
else {
  echo "The $app web application is still not created." 
  echo "Start to create a new $app application...."
  echo "1. Create a ${pool} app pool..."
  # Select each pool object's name property to be a string of the allpools string array.
  $allpools = Get-ChildItem IIS:\AppPools\ | ForEach{"$($_.name)"}
  echo "-----------All Pools----------"
  echo $allpools
  foreach($p in $allpools){
    if ($p.ToLower() -eq $pool.ToLower()) {
	  echo "Remove old pool - $pool and then create a new app pool for $app application."
	  Remove-WebAppPool -Name $p
	  echo "The old pool is removed....."
	  break
	}
  }
  $s2 = "IIS:\AppPools\$($pool)"
  New-WebAppPool -Name $pool
  echo "The new pool is created....."
  echo "Set pool to adopt .net framework 4.0...."
  # set .net framework version 4.0 for new pool
  Set-ItemProperty $s2 -Name managedRuntimeVersion -Value 'v4.0'
  echo "Finish New application pool creation."
  echo "2. Create a new $app web application."
  $s3 = "IIS:\Sites\Default Web Site\$($app)"
  $s4 = "D:\inetpub\LMPI\$($app)_App"
  # Create an empty web application folder.
  if(!(Test-Path -Path $s4 )){
    New-Item -ItemType directory -Path $s4
  }
  # Create an empty log folder
  $logf = "D:\Logfiles2"
  if(!(Test-Path -Path $logf)) {
    New-Item -ItemType directory -Path $logf
	#Set read-write permission for IIS Users.
	$Acl1 = Get-Acl $logf
	$Rights = [System.Security.AccessControl.FileSystemRights]"ReadAndExecute,Write"
	$rule1 = New-Object System.Security.AccessControl.FileSystemAccessRule("BUILTIN\IIS_IUSRS",$Rights,"Allow")
	$Acl1.AddAccessRule($rule1)
	Set-Acl $logf $Acl1
	Get-Acl $logf | Format-List
  }
  # Create web application.
  New-Item $s3 -Type Application -PhysicalPath $s4
  # another web app creation way: New-WebApplication -Name "TestApp" -Site "Default Web Site" -PhysicalPath "$Env:systemdrive\inetpub\TestApp"
  $s = Get-WebApplication | Out-String
  Write-Host $s
  # Set Application pool for new web application.
  Set-ItemProperty $s3 -Name applicationPool -Value $pool
  echo "The Application $($app) has been created."
  # --Remove web application--
  # Remove-WebApplication -Name $app -Site "Default Web Site"
  # ----
  # --Set web appliocation physical path--
  # Set-ItemProperty 'IIS:\Sites\Default Web Site\LMPI' -Name physicalPath -Value D:\Inetpub\LMPI\LMPI_APP
  # ----
}

# return value.
return $true