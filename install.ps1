if (-Not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

if (-not $env:VIRTUAL_ENV) {
    Write-Host "Activating venv..."
    .\venv\Scripts\activate
}

Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

$packages = @(
    "pygame==2.6.1",
    "PyOpenGL==3.1.9"    
)

foreach ($package in $packages) {
    Write-Host "Installing $pkg..."
    pip install $package
}

Write-Host "Finished!"
