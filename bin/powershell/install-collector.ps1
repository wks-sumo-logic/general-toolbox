$sumotoken = $args[0]

$sumoinstalldir = "C:\temp\sumo"

Write-Host New-Item -ItemType Directory -Force -Path $sumoinstalldir

$sumodownloadexe = 'C:\Windows\Temp\SumoCollector.exe'

$sumodownloadurl = 'https://collectors.us2.sumologic.com/rest/download/win64' 

Write-Host Invoke-WebRequest $sumodownloadurl -outfile $sumodownloadexe

$sumocollectorexe = 'C:\Windows\Temp\SumoCollector.exe'

Write-Host $sumocollectorexe -console -q -Vclobber=True "-Vsumo.token_and_url=$sumotoken" "-Vsources=$sumoinstalldir\sources.json" "-Vwrapper.java.maxmemory=512" "-Vcategory=/prod/IRT/server"
