[Setup]
AppName=KodPixel-X-Second-Timer
AppVersion=0.9
AppVerName=KodPixel-X-Second-Timer-0.9
DefaultDirName={pf}\KodPixel-X-Second-Timer
OutputBaseFilename=KodPixel-X-Second-Timer-Setup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
SetupIconFile=C:\KodPixel-X-Second-Timer.ico

[Files]
Source: "C:\KodPixel-X-Second-Timer.exe"; DestDir: "{app}"; Flags: ignoreversion

Source: "C:\KodPixel-X-Second-Timer.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\KodPixel-X-Timer-Second"; \
Filename: "{app}\KodPixel-X-Second-Timer.exe"; \
IconFilename: "{app}\KodPixel-X-Second-Timer.ico"

Name: "{userdesktop}\KodPixel-X-Timer-Second"; \
Filename: "{app}\KodPixel-X-Second-Timer.exe"; \
IconFilename: "{app}\KodPixel-X-Second-Timer.ico"

[Run]
Filename: "{app}\KodPixel-X-Second-Timer.exe"; \
Description: "Launch KodPixel-X-Timer-Second"; \
Flags: nowait postinstall skipifsilent
