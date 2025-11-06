import os, json
from nbformat import read


class AssignmentPreprocessor:
    def __init__(self, data_dir='data', output_dir='processed_data'):
        self.data_dir = data_dir
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)


    def extract_from_py(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()


    def extract_from_ipynb(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            nb = read(f, as_version=4)
        cells = []
        for cell in nb['cells']:
            if cell['cell_type'] in ['markdown', 'code']:
                cells.append(cell['source'])
        return '\n'.join(cells)


    def process_all(self):
        for file in os.listdir(self.data_dir):
            src = os.path.join(self.data_dir, file)
            if file.endswith('.py'):
                text = self.extract_from_py(src)
            elif file.endswith('.ipynb'):
                    text = self.extract_from_ipynb(src)
            else:
                continue


            out_file = os.path.join(self.output_dir, os.path.splitext(file)[0] + '.txt')
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(text)
        print('✅ Preprocessing complete. Text files saved in processed_data/')