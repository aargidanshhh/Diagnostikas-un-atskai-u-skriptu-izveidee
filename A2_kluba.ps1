Get-Service |
    Where-Object { $_.Status.ToString() -eq "Running" } |
    Sort-Object Name |
    Select-Object Name, Status

