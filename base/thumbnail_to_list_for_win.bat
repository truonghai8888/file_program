@echo off
setlocal
rem code dưới đây dùng để thay đổi từ các hình ảnh thu nhỏ của 1 ứng dụng thành cách hiển thị danh sách list
rem ứng dụng được trên cả win 10 và win 11
rem ko yêu cầu quyền admin khi chạy
rem key search Change Taskbar Thumbnail Threshold to Show List in Windows 10
rem Định nghĩa đường dẫn registry và tên giá trị
set "registry_path=HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Taskband"
set "value_name=NumThumbnails"
set "value_data=1"

rem Thêm giá trị DWORD vào registry
reg add "%registry_path%" /v "%value_name%" /t REG_DWORD /d %value_data% /f

if %errorlevel% equ 0 (
    echo Tao gia tri DWORD "%value_name%" voi du lieu "%value_data%" thanh cong.
) else (
    echo Da xay ra loi khi tao gia tri DWORD.
)

endlocal
pause
