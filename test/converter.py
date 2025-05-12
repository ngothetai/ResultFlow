# pip install pandas openpyxl docxtpl
import pandas as pd
from docxtpl import DocxTemplate
from datetime import datetime
import subprocess
import os

# 1. Đọc Excel
data = pd.read_excel('/home/hieudo/CodeSpace/ResultFlow/data/samples/sources/Danh sách BNXN1.xlsx')

for index, row in data.iterrows():
    # 2. Load template
    doc = DocxTemplate('/home/hieudo/CodeSpace/ResultFlow/data/samples/sources/KQ XN.docx')
    
    # 3. Context
    context = {
        'TT': row['TT'],
        'HoVaTen': row['Họ và tên'],
        'Tuoi': row['Tuổi'],
        'GT': row['GT'],
        'DienThoai': row['Điện thoại'],
        'ChanDoan': row['Chẩn đoán'],
        'DonViYeuCau': row['Đơn vị yêu cầu'],
        'NgayLayMau': row['Ngày lấy mẫu'],
        'NgayThucHienXN': row['Ngày thực hiện XN'],
        'KetQua': row['Kết quả'],
    }
    
    # 4. Render
    doc.render(context)
    
    # 5. Lưu Word file
    filename_base = row['TT']
    output_docx = f"/home/hieudo/CodeSpace/ResultFlow/data/samples/results/{filename_base}.docx"
    doc.save(output_docx)
    
    # 6. Convert Word -> PDF bằng LibreOffice (soffice)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", output_docx])

print("Đã tạo xong tất cả PDF.")
