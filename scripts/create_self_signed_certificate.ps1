# Create a self signed certificate
$certSplat = @{
    DnsName = 'constructor@anaconda.com'
    Type = 'CodeSigning'
    NotAfter = (Get-Date).AddDays(365)
    CertStoreLocation = 'cert:\CurrentUser\My'
}
$myCert = New-SelfSignedCertificate @certSplat
$myPwd = ConvertTo-SecureString -String "$env:CONSTRUCTOR_PFX_CERTIFICATE_PASSWORD" -Force -AsPlainText
$pfxSplat = @{
    Cert = $myCert
    FilePath = "$env:CONSTRUCTOR_SIGNING_CERTIFICATE"
    #Password = $myPwd
}
Export-PfxCertificate @pfxSplat
