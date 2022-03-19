$convertDate = Get-Date -format "yyyyMMdd"

$inputFile = $args[0]

$FullPathName = Resolve-Path $inputFile | %{ $_.Path }

$backupFile = $FullPathName.$convertDate.txt

$ExistingKey = $args[1]

$NewValue = $args[2]

Copy-Item -Path $inputFile -Destination $backupFile

$UserPropertiesHash = ConvertFrom-StringData( Get-Content $inputFile -raw )

$UserPropertiesHash[$TestKey] = NewValue

$UserPropertiesHash.GetEnumerator() | % { "$($_.Name)=$($_.Value)" } > $inputFile
