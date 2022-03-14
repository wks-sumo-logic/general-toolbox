### Action: Setup Date
$date = (Get-Date -f yyyyMMddTHHmmss)

### Action: 
$targetPath = “\\<server name>\<share name>\” + $env:ComputerName + "_" + $date

# create folder
new-item -type directory $targetPath

# copy SCCM logs
new-item -type directory $targetPath\SCCM-Logs
copy-item $env:windir\CCM\Logs\* $targetPath\SCCM-Logs

# run gpresult
gpresult /scope computer /h $targetPath\gp_result.html

# get Windows Update log
if ((Get-WmiObject -class Win32_OperatingSystem).version -lt 9) {
    Copy-Item "C:\Windows\WindowsUpdate.log" $targetPath\WindowsUpdateLog.log
} else { 
    get-windowsupdatelog -LogPath $targetpath\WindowsUpdateLog.log 
}

# export event logs
$eventLogsPath = "$targetPath\Event-Logs"
new-item -type directory $eventLogsPath
wevtutil epl System $eventLogsPath\system-event-log.evtx
wevtutil epl Application $eventLogsPath\application-event-log.evtx
wevtutil epl Microsoft-Windows-MBAM/Admin $eventLogsPath\mbam-admin-event-log.evtx
wevtutil epl Microsoft-Windows-MBAM/Operational $eventLogsPath\mbam-operational-event-log.evtx
wevtutil epl "Microsoft-Windows-BitLocker/BitLocker Management" $eventLogsPath\bitlocker-mgmt-event-log.evtx
wevtutil epl "Microsoft-Windows-BitLocker/BitLocker Operational" $eventLogsPath\bitlocker-operational-event-log.evtx
wevtutil epl "Key Management Service" $eventLogsPath\kms-event-log.evtx
wevtutil epl "Microsoft-Windows-Windows Defender/Operational" $eventLogsPath\defender-operational-event-log.evtx

### Define Functions

Set-Variable logFile -Scope Script

function LogInfo($message){Add-Content "$targetPath\$Script:logFile" "$message`n"}

function ConfigureLogger(){$Script:logFile="LogCollections.log"
	Add-Content "$targetPath\$logFile" "Logging..."}

### Function to get System info

function GetSysInfo{
    $sOS =Get-WmiObject -class Win32_OperatingSystem
    LogInfo ("System information...")
    LogInfo ("`t `t `t HostName : " + $env:computername)
    foreach($sProperty in $sOS)
    {
       LogInfo ("`t `t `t OS : " + $sProperty.Caption)
       LogInfo ("`t `t `t OS Architecture : " + $sProperty.OSArchitecture)
       LogInfo ("`t `t `t Service Pack : " + $sProperty.ServicePackMajorVersion)
    }
}

### Function: Gather logs
function GatherLogs(){
  # Collect the IPConfig /All
  LogInfo ("`t - Collecting : IPConfig")
  $colItems = Get-WmiObject -class "Win32_NetworkAdapterConfiguration" | Where {$_.IPEnabled -Match "True"}
  foreach ($objItem in $colItems) {      
       LogInfo ("`t `t `t `t " + $objItem.Description)
       LogInfo ("`t `t `t `t `t `t `t `t `t `t `t Physical Address. . . . . . . . . : " + $objItem.MACAddress)
       LogInfo ("`t `t `t `t `t `t `t `t `t `t `t IPv4v6 Address. . . . . . . . . . : " + $objItem.IPAddress)
       LogInfo ("`t `t `t `t `t `t `t `t `t `t `t Subnet Mask . . . . . . . . . . . : " + $objItem.IPSubnet)
       LogInfo ("`t `t `t `t `t `t `t `t `t `t `t IPEnabled . . . . . . . . . . . . : " + $objItem.IPEnabled)
       LogInfo ("`t `t `t `t `t `t `t `t `t `t `t DNS Servers . . . . . . . . . . . : " + $objItem.DNSServerSearchOrder)
       LogInfo ("`t `t `t `t `t `t `t `t `t `t `t DHCP Server . . . . . . . . . . . : " + $objItem.DHCPServer)
       LogInfo ("`t `t `t `t `t `t `t `t `t `t `t DNS Suffix Search List. . . . . . : " + $objItem.DNSDomainSuffixSearchOrder)
    }
  
  # Applications installed
  $InstalledApp = Wmic Product | Format-Table -AutoSize | Out-String -Width 1024 | Out-File ($targetPath + "\SoftwareInstalled.txt")
  LogInfo ("`t - Collecting : Installed Applications") 
        
  # MS Patches installed
  $InstalledUpdates = WMIC QFE GET | Format-Table -AutoSize | Out-String -Width 1024 | Out-File ($targetPath + "\SoftwareUpdate.txt")
  LogInfo ("`t - Collecting : Installed MS Patches") 
 }

########################################################################################
# Call Functions
########################################################################################

# Setup the log file
ConfigureLogger

# Get System information
GetSysInfo

# Gather logs and other information
LogInfo (“`nGathering required information...")
GatherLogs

#Transcription 
#Start-Transcript -path "$targetPath\$Script:logFile"
#Stop-Transcript
LogInfo ("End.")

#=======================================================================================
# end of MS script

if (Test-Path $TargetPath) {
  Write-Output 0
}
else {
  Write-Output -1
}
