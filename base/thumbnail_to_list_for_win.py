'''
code dưới đây dùng để thay đổi từ các hình ảnh thu nhỏ của 1 ứng dụng thành cách hiển thị danh sách list
ứng dụng được trên cả win 10 và win 11
ko yêu cầu quyền admin khi chạy
cần cài đặt python về sau có thể nâng cấp thành file exe
key search Change Taskbar Thumbnail Threshold to Show List in Windows 10
https://www.thewindowsclub.com/make-taskbar-show-list-instead-of-thumbnail-in-windows
'''


import winreg as reg

# Định nghĩa khóa registry và tên giá trị cần tạo
registry_path = r'Software\Microsoft\Windows\CurrentVersion\Explorer\Taskband'
value_name = 'NumThumbnails'
value_data = 1  # Giá trị DWORD muốn tạo

# Mở khóa registry
try:
    registry_key = reg.OpenKey(reg.HKEY_CURRENT_USER, registry_path, 0, reg.KEY_WRITE)
except FileNotFoundError:
    # Nếu khóa không tồn tại, tạo mới khóa đó
    registry_key = reg.CreateKey(reg.HKEY_CURRENT_USER, registry_path)

# Tạo giá trị DWORD mới
try:
    reg.SetValueEx(registry_key, value_name, 0, reg.REG_DWORD, value_data)
    print(f"Tạo giá trị DWORD '{value_name}' với dữ liệu '{value_data}' thành công.")
    print("Vui lòng reset lại máy tính")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

# Đóng khóa registry
reg.CloseKey(registry_key)
