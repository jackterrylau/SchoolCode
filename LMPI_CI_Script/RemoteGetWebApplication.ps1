$scriptBlock = {
  Import-Module WebAdministration
  Get-WebApplication
}
Invoke-Command ¡VComputerName tw-pls-qa-pis ¡VScriptBlock $scriptBlock 