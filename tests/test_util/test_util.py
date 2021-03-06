from tests.conftest import TEMP_DATA_DIR
from wildebeest.util import find_files_with_extensions


def test_find_files_with_extensions_without_dot(generate_file_tree):
    txt_paths = find_files_with_extensions(search_dir=TEMP_DATA_DIR, extensions=['txt'])
    assert all(path.exists() for path in txt_paths)
    assert len(txt_paths) == 2


def test_find_files_with_extensions_with_dot(generate_file_tree):
    pdf_paths = find_files_with_extensions(
        search_dir=TEMP_DATA_DIR, extensions=['.pdf']
    )
    assert all(path.exists() for path in pdf_paths)
    assert len(pdf_paths) == 1


def test_find_files_with_extensions_str(generate_file_tree):
    pdf_paths = find_files_with_extensions(
        search_dir=str(TEMP_DATA_DIR), extensions=['.pdf']
    )
    assert all(path.exists() for path in pdf_paths)
    assert len(pdf_paths) == 1
