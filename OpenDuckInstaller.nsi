; 脚本使用 Unicode 版本
Unicode True

; 基础设置
Name "OpenDuck Installer"
OutFile "OpenDuck_Installer.exe"
RequestExecutionLevel user ; 需要管理员权限
SetCompressor /SOLID lzma  ; 使用高效压缩

; 安装目录设置
InstallDir "$PROGRAMFILES\OpenDuck"
InstallDirRegKey HKLM "Software\OpenDuck" "Install_Dir" ; <--- 修正关键行

!include MUI2.nsh

; 界面配置
!define MUI_ABORTWARNING  ; 取消安装时显示警告

; 安装页面顺序
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

; 卸载页面顺序
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

; 设置界面语言
!insertmacro MUI_LANGUAGE "English"

; 主安装区段
Section "OpenDuck (required)"
    SectionIn RO  ; 必须安装

    ; 设置输出路径
    SetOutPath $INSTDIR

    ; 打包整个OpenDuck文件夹（假设脚本与OpenDuck文件夹同级）
    File /r "OpenDuck\*.*"

    ; 写入安装信息到注册表
    WriteRegStr HKLM "Software\OpenDuck" "Install_Dir" "$INSTDIR"

    ; 创建卸载程序
    WriteUninstaller "$INSTDIR\Uninstall.exe"

    ; 添加控制面板卸载项
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\OpenDuck" "DisplayName" "OpenDuck"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\OpenDuck" "UninstallString" '"$INSTDIR\Uninstall.exe"'
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\OpenDuck" "InstallLocation" "$INSTDIR"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\OpenDuck" "Publisher" "Your Company"
SectionEnd

; 创建快捷方式（可选区段）
Section "Start Menu Shortcuts"
    CreateDirectory "$SMPROGRAMS\OpenDuck"
    CreateShortcut "$SMPROGRAMS\OpenDuck\Uninstall.lnk" "$INSTDIR\Uninstall.exe"
    CreateShortcut "$SMPROGRAMS\OpenDuck\OpenDuck.lnk" "$INSTDIR\OpenDuckManager.exe"
SectionEnd

Section "Desktop Shortcut"
    CreateShortcut "$DESKTOP\OpenDuck.lnk" "$INSTDIR\OpenDuckManager.exe"
SectionEnd

; 卸载区段
Section "Uninstall"
    ; 删除安装目录
    RMDir /r "$INSTDIR"

    ; 删除开始菜单快捷方式
    RMDir /r "$SMPROGRAMS\OpenDuck"

    ; 删除桌面快捷方式
    Delete "$DESKTOP\OpenDuck.lnk"

    ; 删除注册表项
    DeleteRegKey HKLM "Software\OpenDuck"
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\OpenDuck"
SectionEnd