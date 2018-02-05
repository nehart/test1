; -- Components.iss --
; Demonstrates a components-based installation.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

#define ver "1.0"
#define exe "jep-20180103_1600.exe"
#define name "jep"

[Setup]
AppName={#name}
AppVersion={#ver}
DefaultDirName={pf}\{#name}
DefaultGroupName={#name}
UninstallDisplayIcon={app}\{#exe}

Compression=lzma
SolidCompression=yes

OutputBaseFilename=setup
OutputDir=.\

DisableDirPage=yes
DisableStartupPrompt=yes
DisableProgramGroupPage=yes
DisableReadyPage=yes
DisableFinishedPage=yes
DisableReadyMemo=yes

[Files]
Source: "{#exe}"; DestDir: "{app}"

[Icons]
Name: "{group}\{#name}"; Filename: "{app}\{#exe}"
Name: "{group}\Uninstall"; Filename: "{uninstallexe}"
