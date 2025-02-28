import clang.cindex

def extract_functions_with_clang(file_path):
    index = clang.cindex.Index.create()
    translation_unit = index.parse(file_path, args=['-std=c++17'])
    
    functions = {}
    
    for node in translation_unit.cursor.get_children():
        # 実行ファイルのみ抽出する
        if node.extent.start.file.name != file_path:
            continue
        
        # ファイル内に直接記載されている関数を検出
        if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
            print(node.extent.start.file,node.spelling)
            func_name = node.spelling
            start_line = node.extent.start.line - 1
            start_col = node.extent.start.column - 1
            end_line = node.extent.end.line - 1
            end_col = node.extent.end.column - 1
            
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            func_code_lines = lines[start_line:end_line + 1]
            if len(func_code_lines) > 0:
                func_code_lines[0] = func_code_lines[0][start_col:]
                func_code_lines[-1] = func_code_lines[-1][:end_col]
            
            func_code = ''.join(func_code_lines)
            functions[func_name] = func_code
    
    return functions

cpp_file = "sample.cpp"
functions = extract_functions_with_clang(cpp_file)
# functionsをjsonに変換して保存。
import json
with open("functions.json", "w") as f:
    json.dump(functions, f)

# for name, code in functions.items():
#     print(f"{name}:\n")
#     print(f"{code}")
