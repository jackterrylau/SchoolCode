$scriptBlock = {
  Import-Module WebAdministration
  Get-WebApplication
}
Invoke-Command ˇVComputerName tw-pls-qa-pis ˇVScriptBlock $scriptBlock 