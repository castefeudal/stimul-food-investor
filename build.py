from pathlib import Path
import shutil
root=Path(__file__).parent
shutil.rmtree(root/'dist',ignore_errors=True)
shutil.copytree(root/'src',root/'dist')
print('Готово: папка dist обновлена')
